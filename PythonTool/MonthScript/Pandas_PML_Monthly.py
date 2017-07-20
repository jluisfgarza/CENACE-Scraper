# Author:
#    Juan Luis Flores Garza
# Date: 7/20/2017
#
# Downloader for PML - (Precios Nodos Distribuidos)

import pandas as pd
import os
import time
import sqlalchemy as sa
from datetime import datetime

# Global Variables
    # Arrays with list of paths for MDA and MTR
pathlist_MDA = []
pathlist_MTR = []
    # Path of directories with csv files
MTR_path = "C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/PythonTool/TestCSVdirMonth/PML/MTR/"
MDA_path = "C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/PythonTool/TestCSVdirMonth/PML/MDA/"
    # Pandas DataFrame
coleccionPML = pd.DataFrame()
    # Helper Variables for integrity check
regcount = 0
initregcount = 0
initPML = 0
    # SQL CONNECTION ENGINE
engine = sa.create_engine('mssql+pyodbc://E-JLFLORESG/PreciosEnergia?driver=SQL+Server+Native+Client+11.0')

################################ try_parsing_date ###############################
# Helper Function to parse different date formats into MM/DD/YYYY
def try_parsing_date(text):
    for fmt in ('%Y/%m/%d', '%d/%m/%Y'):
        try:
            mydate = datetime.strptime(text, fmt)
            return datetime.strftime(mydate, "%m/%d/%Y")
        except ValueError:
            pass
    raise ValueError('no valid date format found ' + text)

#################################### dbcount ###################################
# Function to check amount Reg at DB at PML table
def dbcount():
    global engine
    with engine.connect() as conn, conn.begin():
        # SQl query count rows on PML
        PML = pd.read_sql('SELECT COUNT(*) as [NumRegPML] FROM [PreciosEnergia].[dbo].[PML]', conn)
        PML.reset_index(drop=True)
        TPML = PML.iat[0,0]
        #print ('NumRegPML: %d' % TPML)
    return (TPML)

################################## deletedupPML #################################
# Function to delete duplicated rows
def deletedupPML():
   global engine
   # Using a work arround to print a null while executing a query to delete duplicates in order to be able to execute the CTE query
   with engine.connect() as conn, conn.begin():
       # SQl query count rows on PML
       deltemp = pd.read_sql('SELECT TOP (0) [Hora] FROM [PreciosEnergia].[dbo].[PML]; WITH CTE_Dup AS(SELECT [Nodo], [Hora], [Precio], [Energia], [Perdidas], [Congestion], [Fecha], [Tipo], [Sistema], ROW_NUMBER()OVER(PARTITION BY Nodo, Fecha, Hora, Tipo, Sistema ORDER BY Sistema) as RN FROM [PreciosEnergia].[dbo].[PML]) DELETE FROM CTE_Dup WHERE RN <> 1;', conn)
       print ('Deleted Duplicate Rows' )
   return

################################## getPMLpaths #################################
# Function to get file paths on desired directories
def getPMLpaths(dir1, dir2):
    global pathlist_MDA
    global pathlist_MTR
    #MDA
    for subdir, dirs, files in os.walk(dir1):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".csv"):
                path = filepath
                pathlist_MDA.append(path)
    #MTR
    for subdir, dirs, files in os.walk(dir2):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".csv"):
                path = filepath
                pathlist_MTR.append(path)
    '''
    print (pathlist_MDA)
    print('\n')
    print (pathlist_MTR)
    print('\n')
    '''
    return

################################## uploadtoDB ##################################
# Function that process and inserts data to SQL DB
def uploadtoDB(pathlist1, pathlist2):
    global coleccionPML
    global regcount
    global check
    global initregcount
    global engine
    #MDA
    for element in pathlist1:
        path = element
        #print(path + '\n')
        if path.find('SIN') >= 0:
            sistema = 'SIN'
        if path.find('BCA') >= 0:
            sistema = 'BCA'
        if path.find('BCS') >= 0:
            sistema = 'BCS'
        # Read CSV file
        PML = pd.read_csv(path)
        # Init Columns
        PML.columns = ["Fecha","Hora","Nodo","Precio","Energia","Perdidas","Congestion"]
        PML["Fecha"] = pd.to_datetime(PML.Fecha)
        PML["Tipo"]  = "MDA"
        PML["Sistema"] = sistema
        # Init DataFrame
        coleccionPML.empty
        coleccionPML = pd.DataFrame()
        coleccionPML = coleccionPML.append(PML, ignore_index=True, verify_integrity=True)
        # Data integrity check for number of rows
        PMLcount = PML.Fecha.count()
        regcount = regcount + PMLcount
        print ('Row Count... %d'  % regcount)
        # Open connection to start inserts.
        with engine.connect() as conn, conn.begin():
            coleccionPML.to_sql('PML',
                                engine,
                                if_exists='append',
                                index = False,
                                dtype={'Fecha': sa.DateTime(),
                                       'Hora': sa.types.SmallInteger(),
                                       'Nodo': sa.types.NVARCHAR(length=20),
                                       'Precio': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Energia': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Perdidas': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Congestion': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Tipo': sa.types.NVARCHAR(length=3),
                                       'Sistema': sa.types.NVARCHAR(length=3)})
    #MTR
    for element in pathlist2:
        path = element
        #print(path + '\n')
        if path.find('SIN') >= 0:
            sistema = 'SIN'
        if path.find('BCA') >= 0:
            sistema = 'BCA'
        if path.find('BCS') >= 0:
            sistema = 'BCS'
        # Read CSV file
        PML = pd.read_csv(path)
        # Init Columns
        PML.columns = ["Fecha","Hora","Nodo","Precio","Energia","Perdidas","Congestion"]
        PML["Fecha"] = pd.to_datetime(PML.Fecha)
        PML["tipo"] = "MTR"
        PML["sistema"] = sistema
        # Init DataFrame
        coleccionPML.empty
        coleccionPML = pd.DataFrame()
        coleccionPML = coleccionPML.append(PML, ignore_index=True, verify_integrity=True)
        # Data integrity check for number of rows
        PMLcount = PML.Fecha.count()
        regcount = regcount + PMLcount
        print ('Row Count... %d'  % regcount)
        # Open connection to start inserts.
        with engine.connect() as conn, conn.begin():
            coleccionPML.to_sql('PML',
                                engine,
                                if_exists='append',
                                index = False,
                                dtype={'Fecha': sa.DateTime(),
                                       'Hora': sa.types.SmallInteger(),
                                       'Nodo': sa.types.NVARCHAR(length=20),
                                       'Precio': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Energia': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Perdidas': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Congestion': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Tipo': sa.types.NVARCHAR(length=3),
                                       'Sistema': sa.types.NVARCHAR(length=3)})
    # Ignore DataFrame index
    coleccionPML.reset_index(drop=True)
    # Get amount of reg on DB
    dbsize = dbcount()
    # If DB size equals the starting number of reg + the number of inserts
    if (initregcount + regcount == dbsize):
        print ('Size Check... PASSED')
        print ('DB Initial Size: %d' % initregcount)
        print ('After Script Size: %d' % dbsize)
        check = True
    # If DB size is different from the starting number of reg + the number of inserts
    if (initregcount + regcount != dbsize):
        print ('Size Check... ERROR')
        print ('Restarting script...')
        print ('DB Initial Size: %d' % initregcount)
        print ('After Script Size: %d' %  dbsize)
        check = False
    return

################################# Main Program #################################
def mainprogram():
    global check
    global pathlist_MDA
    global pathlist_MTR
    global coleccionPML
    global regcount
    # Get paths
    getPMLpaths(MDA_path, MTR_path)
    # Send path lists
    uploadtoDB(pathlist_MDA, pathlist_MTR)
    # If integrity check = PASSED
    if (check == True):
        print ('Excecution Complete.')
    # If integrity check != PASSED, repeat process
    if (check == False):
        # Clean variables, DataFrame and delete repeated rows on DB
        pathlist_MDA = []
        pathlist_MTR = []
        coleccionPML.empty
        coleccionPML = pd.DataFrame()
        regcount = 0
        check = False
        deletedupPML()
        mainprogram()
    return

#################################### Start #####################################
# Compare initial DB size and after execution size
print("____________________________")
print("--- Starting Monthly PML ---")
initregcount = dbcount()
print ('DB Initial Size: %d' % initregcount)
start_time = time.time()
mainprogram()
deletedupPML()
finalcount = dbcount()
print ('Final DB Size: %d' % finalcount)
print("Execution time: %s seconds" % (time.time() - start_time))
print("____________________________")
