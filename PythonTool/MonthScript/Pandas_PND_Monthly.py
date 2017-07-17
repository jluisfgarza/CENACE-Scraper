# Author:
#    Juan Luis Flores Garza
# Date: 7/17/2017
#
# Downloader for PND - (Precios Nodos Distribuidos)

import pandas as pd
import os
import time
import sqlalchemy as sa

# Global Variables
pathlist_MDA = []
pathlist_MTR = []
MDA_path = "C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/PythonTool/TestCSVdirMonth/PND/MDA/"
MTR_path = "C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/PythonTool/TestCSVdirMonth/PND/MTR/"
coleccionPND = pd.DataFrame()
regcount = 0
check = False

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
    """
    print (pathlist_MDA)
    print('\n')
    print (pathlist_MTR)
    print('\n')
    """
    return

def uploadtoDB(pathlist1, pathlist2):

    global coleccionPND
    global regcount
    global check

    #MDA
    for element in pathlist1:
        path = element
        print(path + '\n')

        if path.find('SIN') >= 0:
            sistema = 'SIN'
        if path.find('BCA') >= 0:
            sistema = 'BCA'
        if path.find('BCS') >= 0:
            sistema = 'BCS'

        PND = pd.read_csv(path)
        # Init Columns
        PND.columns = ["Fecha","Hora","Zona de Carga","Precio Zonal","Energia","Perdidas","Congestion"]
        PND["tipo"] = "MDA"
        PND["sistema"] = sistema
        coleccionPND = coleccionPND.append(PND, ignore_index=True)
        PNDcount = PND.Fecha.count()
        regcount = regcount + PNDcount

    #MTR
    for element in pathlist2:
        path = element
        print(path + '\n')

        if path.find('SIN') >= 0:
            sistema = 'SIN'
        if path.find('BCA') >= 0:
            sistema = 'BCA'
        if path.find('BCS') >= 0:
            sistema = 'BCS'

        PND = pd.read_csv(path)
        # Init Columns
        PND.columns = ["Fecha","Hora","Zona de Carga","Precio Zonal","Energia","Perdidas","Congestion"]
        PND["tipo"] = "MTR"
        PND["sistema"] = sistema
        coleccionPND = coleccionPND.append(PND, ignore_index=True)
        PNDcount = PND.Fecha.count()
        regcount = regcount + PNDcount

    coleccionPND.reset_index(drop=True)
    # Export CSV or database
    mydate = time.strftime("%B-%Y")
    # Data integrity check for number of rows
    DataframetoimportSize = coleccionPND.Hora.count()
    if (DataframetoimportSize == regcount):
        print ('size check... PASSED')
        print ('Data Frame Size: %d'  % DataframetoimportSize)
        print ('Check Number: %d'  %  regcount)
        check = True
        print (coleccionPND)
        coleccionPND.to_csv('C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/PythonTool/PastCSVBackup/PND/PND-' + mydate + '.csv', index = False)
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
    global coleccionPND
    global regcount

    getPNDpaths(MDA_path, MTR_path)
    uploadtoDB(pathlist_MDA, pathlist_MTR)

    if (check == True):
        print ('Importing to Local SQL DB.')
        engine = sa.create_engine('mssql+pyodbc://E-JLFLORESG/PreciosEnergia?driver=SQL+Server+Native+Client+11.0')
        with engine.connect() as conn, conn.begin():
            coleccionPND.to_sql('PND',
                                engine,
                                if_exists='append',
                                index = False,
                                dtype={'Fecha': sa.DateTime(),
                                       'Hora': sa.types.SmallInteger(),
                                       'Zona de Carga': sa.types.NVARCHAR(length=20),
                                       'Precio Zonal': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Energia': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Perdidas': sa.types.DECIMAL(precision=2, asdecimal=True),
                                       'Congestion': sa.types.NVARCHAR(length=10),
                                       'Tipo': sa.types.NVARCHAR(length=3),
                                       'Sistema': sa.types.NVARCHAR(length=3)})
        print ('Excecution Complete.')
        
    if (check == False):
        pathlist_MDA = []
        pathlist_MTR = []
        coleccionPND.empty
        coleccionPND = pd.DataFrame()
        regcount = 0
        check = False
        mainprogram()

    return

mainprogram()
