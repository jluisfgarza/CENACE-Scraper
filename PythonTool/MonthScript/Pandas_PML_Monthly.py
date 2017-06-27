# Authors:
#    Fransisco Con Garza
#    Ricardo Alatorre Cantú
#    Juan Luis Flores Garza
# Date: 6/21/2017
#
# Downloader for PML - (Precios Nodos Distribuidos)

import pandas as pd
import os
import datetime
import time
import csv


# Global Variables
pathlist_MDA = []
pathlist_MTR = []
MDA_path = "C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/PythonTool/PastCSVBackup/PML/MDA/"
MTR_path = "C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/PythonTool/PastCSVBackup/PML/MTR"
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
    print (pathlist_MDA)
    print('\n')
    print (pathlist_MTR)
    print('\n')

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

        with open(path, newline='') as f:
          reader = csv.reader(f)
          row1 = str(next(reader))
          #print (row1)
        PML = pd.read_csv(path, nrows=1)
        # Init Columns
        PML.columns = ["Fecha","Hora","Zona de Carga","Precio Zonal","Energía","Pérdidas","Congestión"]

        if row1.find('Centro Nacional de Control de Energia') >= 0:
            PML = pd.read_csv(path, skiprows=[0,1,2,3,4,5,6])

        if row1.find('Precios de energia en nodos distribuidos del MDA') >= 0:
            PML = pd.read_csv(path, skiprows=[0,1,2,3,4,5])

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

        with open(path, newline='') as f:
            reader = csv.reader(f)
            row1 = str(next(reader))
            #print (row1)
        PML = pd.read_csv(path, nrows=1)
        # Init Columns
        PML.columns = ["Fecha","Hora","Zona de Carga","Precio Zonal","Energía","Pérdidas","Congestión"]

        if row1.find('Centro Nacional de Control de Energia') >= 0:
            PML = pd.read_csv(path, skiprows=[0,1,2,3,4,5,6])

        if row1.find('Precios de energia en nodos distribuidos del MDA') >= 0:
            PML = pd.read_csv(path, skiprows=[0,1,2,3,4,5])

        PML["tipo"] = "MTR"
        PML["sistema"] = sistema
        coleccionPML = coleccionPML.append(PML, ignore_index=True)
        PMLcount = PML.Fecha.count()
        regcount = regcount + PMLcount

    coleccionPML.reset_index(drop=True)
    # Export CSV or database
    ## dd/mm/yyyy format
    mydate = time.strftime("%d-%m-%Y")
    # Data integrity check for number of rows
    DataframetoimportSize = coleccionPML.Hora.count()
    if (DataframetoimportSize == regcount):
        print ('size check... PASSED')
        print ('Data Frame Size: %d'  % DataframetoimportSize)
        print ('Check Number: %d'  %  regcount)
        check = True
        coleccionPML.to_csv('C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/PythonTool/PastCSVBackup/PML/' + mydate + '.csv', index = False)
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
