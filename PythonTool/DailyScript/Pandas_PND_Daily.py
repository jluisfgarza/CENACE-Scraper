# Author:
#    Juan Luis Flores Garza
# Date: 6/21/2017
#
# Downloader for PND - (Precios Nodos Distribuidos)

import pandas as pd
import os
import time
import csv
import sqlalchemy as sa
import dateparser

# Global Variables
    # Arrays with list of paths for MDA and MTR
pathlist_MDA = []
pathlist_MTR = []
    # Path of directories with csv files
MDA_path = "C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/PythonTool/TestCSVdirDaily/PND/MDA/"
MTR_path = "C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/PythonTool/TestCSVdirDaily/PND/MTR/"
    # Pandas DataFrame
coleccionPND = pd.DataFrame()
    # Helper Variables for integrity check
regcount = 0
initregcount = 0
check = False
initPND = 0
    # SQL CONNECTION ENGINE
engine = sa.create_engine('mssql+pyodbc://E-JLFLORESG/PreciosEnergia?driver=SQL+Server+Native+Client+11.0')

#################################### dbcount ###################################
# Function to check amount Reg at DB at PND table
def dbcount():
    global engine
    with engine.connect() as conn, conn.begin():
        # SQl query count rows on PND
        PND = pd.read_sql('SELECT COUNT(*) as [NumRegPND] FROM [PreciosEnergia].[dbo].[PND]', conn)
        PND.reset_index(drop=True)
        TPND = PND.iat[0,0]
        #print ('NumRegPND: %d' % TPND)
    return (TPND)

################################## deletedupPND #################################
# Function to delete duplicated rows
def deletedupPND():
   global engine
   # Using a work arround to print a null while executing a query to delete duplicates in order to be able to execute the CTE query
   with engine.connect() as conn, conn.begin():
       # SQl query count rows on PND
       deltemp = pd.read_sql('SELECT TOP (0) [Hora] FROM [PreciosEnergia].[dbo].[PND]; WITH CTE_Dup AS( SELECT [Zona de Carga], [Hora], [Precio Zonal], [Energia], [Perdidas], [Congestion], [Fecha], [Tipo], [Sistema], ROW_NUMBER()OVER(PARTITION BY [Zona de Carga], Fecha, Hora, Tipo, Sistema ORDER BY Sistema) as RN FROM [PreciosEnergia].[dbo].[PND]) DELETE FROM CTE_Dup WHERE RN <> 1;', conn)
       print ('Deleted Duplicate Rows' )
   return

################################## getPNDpaths #################################
# Function to get file paths on desired directories
def getPNDpaths(dir1, dir2):
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
    global coleccionPND
    global regcount
    global check
    global initregcount
    global engine
    #MDA
    for element in pathlist1:
        path = element
        #print(path + '\n')
        if path.find('_SIN_PreciosNodosDistribuidosMDA') >= 0:
            sistema = 'SIN'
        if path.find('_BCA_PreciosNodosDistribuidosMDA') >= 0:
            sistema = 'BCA'
        if path.find('_BCS_PreciosNodosDistribuidosMDA') >= 0:
            sistema = 'BCS'
        # Read CSV file
        with open(path, newline='') as f:
          reader = csv.reader(f)
          row1 = str(next(reader))
          #print (row1)
        PND = pd.DataFrame()
            # Check header length according to first row content
        if row1.find('Centro Nacional de Control de Energia') >= 0:
            PND = pd.read_csv(path, skiprows=[0,1,2,3,4,5,6])
            # Get the date from CSV header
            fecha = pd.read_csv(path, nrows=1, skiprows=[0,1,2])
        if row1.find('Precios de energia en nodos distribuidos del MDA') >= 0:
            PND = pd.read_csv(path, skiprows=[0,1,2,3,4,5])
            # Get the date from CSV header
            fecha = pd.read_csv(path, nrows=1, skiprows=[0,1])
        # Init Columns
        PND.columns = ["Hora","Zona de Carga","Precio Zonal","Energia","Perdidas","Congestion", "Derp"]
        alfa = fecha["Reporte diario"].to_string(index=False)
        alfa = alfa[-len(alfa)+alfa.index(" ")+1:]
        alfa = ((dateparser.parse(alfa, date_formats=['%d/%B/%Y'], languages=['pt', 'es'])))
        PND["Fecha"] = pd.to_datetime(alfa)
        PND["Tipo"] = "MDA"
        PND["Sistema"] = sistema
        # Init DataFrame
        coleccionPND.empty
        coleccionPND = pd.DataFrame()
        coleccionPND = coleccionPND.append(PND, ignore_index=True, verify_integrity=True)
        # Data integrity check for number of rows
        PNDcount = PND.Hora.count()
        regcount = regcount + PNDcount
        print ('Row Count... %d'  % regcount)
        del coleccionPND["Derp"]
        # Open connection to start inserts.
        with engine.connect() as conn, conn.begin():
            coleccionPND.to_sql('PND',
                                engine,
                                if_exists='append',
                                index = False,
                                dtype={'Fecha': sa.DateTime(),
                                       'Hora': sa.types.SmallInteger(),
                                       'Zona de Carga': sa.types.NVARCHAR(length=20),
                                       'Precio Zona': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Energia': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Perdidas': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Congestion': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Tipo': sa.types.NVARCHAR(length=3),
                                       'Sistema': sa.types.NVARCHAR(length=3)})

    #MTR
    for element in pathlist2:
        path = element
        #print(path + '\n')
        if path.find('PreciosNodosDistrib SIN MTR_') >= 0:
            sistema = 'SIN'
        if path.find('PreciosNodosDistrib BCA MTR_') >= 0:
            sistema = 'BCA'
        if path.find('PreciosNodosDistrib BCS MTR_') >= 0:
            sistema = 'BCS'
         # Read CSV file
        with open(path, newline='') as f:
          reader = csv.reader(f)
          row1 = str(next(reader))
          #print (row1)
        PND = pd.DataFrame()
            # Check header length according to first row content
        if row1.find('Centro Nacional de Control de Energia') >= 0:
            PND = pd.read_csv(path, skiprows=[0,1,2,3,4,5,6])
            # Get the date from CSV header
            fecha = pd.read_csv(path, nrows=1, skiprows=[0,1,2])
        if row1.find('Precios de energia en nodos distribuidos del MTR') >= 0:
            PND = pd.read_csv(path, skiprows=[0,1,2,3,4,5])
            # Get the date from CSV header
            fecha = pd.read_csv(path, nrows=1, skiprows=[0,1])
        # Init Columns
        PND.columns = ["Hora","Zona de Carga","Precio Zonal","Energia","Perdidas","Congestion", "Derp"]
        alfa = fecha["Reporte diario"].to_string(index=False)
        alfa = alfa[-len(alfa)+alfa.index(" ")+1:]
        alfa = ((dateparser.parse(alfa, date_formats=['%d/%B/%Y'], languages=['pt', 'es'])))
        PND["Fecha"] = pd.to_datetime(alfa)
        PND["Tipo"] = "MTR"
        PND["Sistema"] = sistema
        # Init DataFrame
        coleccionPND.empty
        coleccionPND = pd.DataFrame()
        coleccionPND = coleccionPND.append(PND, ignore_index=True, verify_integrity=True)
        # Data integrity check for number of rows
        PNDcount = PND.Hora.count()
        regcount = regcount + PNDcount
        print ('Row Count... %d'  % regcount)
        del coleccionPND["Derp"]
        # Open connection to start inserts.
        with engine.connect() as conn, conn.begin():
            coleccionPND.to_sql('PND',
                                engine,
                                if_exists='append',
                                index = False,
                                dtype={'Fecha': sa.DateTime(),
                                       'Hora': sa.types.SmallInteger(),
                                       'Zona de Carga': sa.types.NVARCHAR(length=20),
                                       'Precio Zona': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Energia': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Perdidas': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Congestion': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Tipo': sa.types.NVARCHAR(length=3),
                                       'Sistema': sa.types.NVARCHAR(length=3)})

    # Ignore DataFrame index
    coleccionPND.reset_index(drop=True)
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

################################# Main Program ################################
def mainprogram():
    global check
    global pathlist_MDA
    global pathlist_MTR
    global coleccionPND
    global regcount
    # Get paths
    getPNDpaths(MDA_path, MTR_path)
    # Send path lists
    uploadtoDB(pathlist_MDA, pathlist_MTR)
    # If integrity check = PASSED
    if (check == True):
        print ('Excecution Complete.')
    # If integrity check != PASSED, repeat process
    if (check == False):
        # Clean variables, DataFrame and delete repeatedrows on DB
        pathlist_MDA = []
        pathlist_MTR = []
        coleccionPND.empty
        coleccionPND = pd.DataFrame()
        regcount = 0
        check = False
        deletedupPND()
        mainprogram()
    return

#################################### Start #####################################
# Compare initial DB size and after execution size
print("____________________________")
print("---- Starting Daily PND ----")
initregcount = dbcount()
print ('DB Initial Size: %d' % initregcount)
start_time = time.time()
mainprogram()
deletedupPND()
finalcount = dbcount()
print ('Final DB Size: %d' % finalcount)
print("Execution time: %s seconds" % (time.time() - start_time))
print("____________________________")
