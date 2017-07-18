# Author:
#    Juan Luis Flores Garza
# Date: 7/17/2017
#
# Downloader for PML - (Precios Nodos Distribuidos)

import pandas as pd
import os
import sqlalchemy as sa

# Global Variables
pathlist_MDA = []
pathlist_MTR = []
MTR_path = "C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/PythonTool/TestCSVdirMonth/PML/MTR/"
MDA_path = "C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/PythonTool/TestCSVdirMonth/PML/MDA/"
coleccionPML = pd.DataFrame()
regcount = 0
initregcount = 0
initPML = 0
    # SQL CONNECTION ENGINE
engine = sa.create_engine('mssql+pyodbc://E-JLFLORESG/PreciosEnergia?driver=SQL+Server+Native+Client+11.0')

# Check amount Reg at DB at Start
def dbcount():
    global engine
    with engine.connect() as conn, conn.begin():            
        # SQl query count rows on PML
        PML = pd.read_sql('SELECT COUNT(*) as [NumRegPML] FROM [PreciosEnergia].[dbo].[PML]', conn)    
        PML.reset_index(drop=True)        
        TPML = PML.iat[0,0]    
        print ('NumRegPML: %d' % TPML)        
    return (TPML)

# Delete duplicated rows
def deletedupPML():
   global engine
   # using a work arround to print a null while executing a query to delete duplicates
   with engine.connect() as conn, conn.begin():            
       # SQl query count rows on PML
       deltemp = pd.read_sql('SELECT TOP (0) [Hora] FROM [PreciosEnergia].[dbo].[PML]; WITH CTE AS( SELECT [Nodo], [Hora], [Precio], [Energia], [Perdidas], [Congestion], [Fecha], [Tipo], [Sistema], RN = ROW_NUMBER()OVER(PARTITION BY Nodo, Fecha, Hora, Tipo, Sistema ORDER BY Sistema) FROM dbo.PML) DELETE FROM CTE WHERE RN > 1;', conn)    
       print ('Deleted Duplicate Rows' )     
   return

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

    
    print (pathlist_MDA)
    print('\n')
    print (pathlist_MTR)
    print('\n')
    
    return

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

        PML = pd.read_csv(path)
        # Init Columns
        PML.columns = ["Fecha","Hora","Nodo","Precio","Energia","Perdidas","Congestion"]
        PML["tipo"]  = "MDA"
        PML["sistema"] = sistema
           
        coleccionPML.empty
        coleccionPML = pd.DataFrame()
        coleccionPML = coleccionPML.append(PML, ignore_index=True, verify_integrity=True)
        # Data integrity check for number of rows
        PMLcount = PML.Fecha.count()
        regcount = regcount + PMLcount
        
        # print ('Importing to Local SQL DB.')
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
                                       'Congestion': sa.types.NVARCHAR(length=10),
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

        PML = pd.read_csv(path)
        # Init Columns
        PML.columns = ["Fecha","Hora","Nodo","Precio","Energia","Perdidas","Congestion"]
        PML["tipo"] = "MTR"
        PML["sistema"] = sistema                    
        
        coleccionPML.empty
        coleccionPML = pd.DataFrame()
        coleccionPML = coleccionPML.append(PML, ignore_index=True, verify_integrity=True)
        # Data integrity check for number of rows
        PMLcount = PML.Fecha.count()
        regcount = regcount + PMLcount
        
        # print ('Importing to Local SQL DB.')
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
                                       'Congestion': sa.types.NVARCHAR(length=10),
                                       'Tipo': sa.types.NVARCHAR(length=3),
                                       'Sistema': sa.types.NVARCHAR(length=3)})  
        
        

    coleccionPML.reset_index(drop=True)

    dbsize = dbcount()
    if (initregcount + regcount == dbsize):
        print ('size check... PASSED')
        print ('Original Size: %d'  % initregcount)
        print ('After Script Size: %d'  %  dbsize)
        check = True
        
    if (initregcount + regcount != dbsize):
        print ('size check... ERROR')
        print ('Restarting script...')
        print ('Original Size: %d'  % initregcount)
        print ('After Script Size: %d'  %  dbsize)
        check = False

    return

################################# Main Program ################################
def mainprogram():
    global check
    global pathlist_MDA
    global pathlist_MTR
    global coleccionPML
    global regcount    

    getPMLpaths(MDA_path, MTR_path)
    uploadtoDB(pathlist_MDA, pathlist_MTR)

    if (check == True):      
        print ('Excecution Complete.')

    if (check == False):
        pathlist_MDA = []
        pathlist_MTR = []
        coleccionPML.empty
        coleccionPML = pd.DataFrame()
        regcount = 0
        check = False
        deletedupPML()
        mainprogram()
        
    return

initregcount = dbcount()
print ('DB Initial Size: %d' % initregcount)
mainprogram()
deletedupPML()
finalcount = dbcount()
print ('Final DB Size: %d' % finalcount)