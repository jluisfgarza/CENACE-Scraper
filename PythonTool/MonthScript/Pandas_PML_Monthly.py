# Author:
#    Juan Luis Flores Garza
# Date: 7/17/2017
#
# Downloader for PML - (Precios Nodos Distribuidos)

import pandas as pd
import os
import time
import sqlalchemy as sa

# Global Variables
pathlist_MDA = []
pathlist_MTR = []
MTR_path = "C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/PythonTool/PastCSVBackup/PML/MTR/"
MDA_path = "C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/PythonTool/PastCSVBackup/PML/MDA/"
coleccionPML = pd.DataFrame()
regcount = 0
check = False

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

    """
    print (pathlist_MDA)
    print('\n')
    print (pathlist_MTR)
    print('\n')
    """
    return

def uploadtoDB(pathlist1, pathlist2):

    global coleccionPML
    global regcount
    global check

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
        PML["tipo"] = "MDA"
        PML["sistema"] = sistema
        coleccionPML = coleccionPML.append(PML, ignore_index=True)
        PMLcount = PML.Fecha.count()
        regcount = regcount + PMLcount

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
        coleccionPML = coleccionPML.append(PML, ignore_index=True)
        PMLcount = PML.Fecha.count()
        regcount = regcount + PMLcount

    coleccionPML.reset_index(drop=True)

    # Export CSV or database
    mydate = time.strftime("%B-%Y")
    # Data integrity check for number of rows
    DataframetoimportSize = coleccionPML.Hora.count()
    if (DataframetoimportSize == regcount):
        print ('size check... PASSED')
        print ('Data Frame Size: %d'  % DataframetoimportSize)
        print ('Check Number: %d'  %  regcount)
        check = True
        print (coleccionPML)
        #coleccionPML.to_csv('C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/PythonTool/PastCSVBackup/PML/PML-' + mydate + '.csv', index = False)
    if (DataframetoimportSize != regcount):
        print ('size check... ERROR')
        print ('Restarting script...')
        print ('Data Frame Size: %d'  % DataframetoimportSize)
        print ('Check Number: %d'  %  regcount)
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
        print ('Importing to Local SQL DB.')
        engine = sa.create_engine('mssql+pyodbc://E-JLFLORESG/PreciosEnergia?driver=SQL+Server+Native+Client+11.0')
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
        print ('Excecution Complete.')

    if (check == False):
        pathlist_MDA = []
        pathlist_MTR = []
        coleccionPML.empty
        coleccionPML = pd.DataFrame()
        regcount = 0
        check = False
        mainprogram()

    return

mainprogram()
