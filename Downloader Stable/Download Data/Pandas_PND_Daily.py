# Authors:
#    Fransisco Con Garza
#    Ricardo Alatorre Cantú
#    Juan Luis Flores Garza
# Date: 6/21/2017
#
# Downloader for PND - (Precios Nodos Distribuidos)

import pandas as pd
import os
import datetime
import locale
import pyodbc
import time

# SQL Server connection
#server = 'your_server.database.windows.net'
#database = 'your_database'
#username = 'your_username'
#password = 'your_password'
#driver= '{ODBC Driver 13 for SQL Server}'
#cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

# INSERT query example
#cursor = cnxn.cursor()
#with cursor.execute("INSERT INTO SalesLT.Product (Name, ProductNumber, Color, StandardCost, ListPrice, SellStartDate) OUTPUT INSERTED.ProductID VALUES ('BrandNewProduct', '200989', 'Blue', 75, 80, '7/1/2016')"):
#    print ('Successfuly Inserted!')
#cnxn.commit()

# Check bulk insert to DB

# Global Variables
pathlist_MDA = []
pathlist_MTR = []
MDA_path = "C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Download Data/CSVdir/PND/MDA/"
MTR_path = "C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Download Data/CSVdir/PND/MTR/"
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

    print (pathlist_MDA)
    print('\n')
    print (pathlist_MTR)
    print('\n')
    return

def uploadtoDB(pathlist1, pathlist2):

    global coleccionPND
    global regcount
    global check

    #MDA
    for element in pathlist1:
        path = element
        print(path + '\n')
        if path.find('_SIN_PreciosNodosDistribuidosMDA') >= 0:
            sistema = 'SIN'
        if path.find('_BCA_PreciosNodosDistribuidosMDA') >= 0:
            sistema = 'BCA'
        if path.find('_BCS_PreciosNodosDistribuidosMDA') >= 0:
            sistema = 'BCS'
        PND = pd.read_csv(path, skiprows=[0,1,2,3,4,5,6])
        # Init Columns
        PND.columns = ["Hora","Zona de Carga","Precio Zonal","Energía","Pérdidas","Congestión", "Derp"]
        # Get the date from CSV header
        fecha = pd.read_csv(path, nrows=1, skiprows=[0,1,2])
        locale.setlocale(locale.LC_TIME, 'es')
        alfa = fecha["Reporte diario"].to_string(index=False)
        # Get substr with the date and format it
            #print(fecha)
        mydate = datetime.datetime.strptime(alfa[-len(alfa)+alfa.index(" ")+1:], '%d/%B/%Y').strftime('%B/%d/%Y')
            #print (mydate)
        mydate = datetime.datetime.strptime(mydate, '%B/%d/%Y')
        PND["timestamp"] = PND["Hora"].apply(lambda x: mydate + datetime.timedelta(hours=int(x)))
        PND["tipo"] = "MDA"
        PND["sistema"] = sistema
        coleccionPND = coleccionPND.append(PND, ignore_index=True)
        PNDcount = PND.Hora.count()
        regcount = regcount + PNDcount

    #MTR
    for element in pathlist2:
        path = element
        print(path + '\n')
        if path.find('PreciosNodosDistrib SIN MTR_') >= 0:
            sistema = 'SIN'
        if path.find('PreciosNodosDistrib BCA MTR_') >= 0:
            sistema = 'BCA'
        if path.find('PreciosNodosDistrib BCS MTR_') >= 0:
            sistema = 'BCS'
        PND = pd.read_csv(path, skiprows=[0,1,2,3,4,5,6])
        # Init Columns
        PND.columns = ["Hora","Zona de Carga","Precio Zonal","Energía","Pérdidas","Congestión", "Derp"]
        # Get the date from CSV header
        fecha = pd.read_csv(path, nrows=1, skiprows=[0,1,2])
        locale.setlocale(locale.LC_TIME, 'es')
        alfa = fecha["Reporte diario"].to_string(index=False)
        # Get substr with the date and format it
            #print(fecha)
        mydate = datetime.datetime.strptime(alfa[-len(alfa)+alfa.index(" ")+1:], '%d/%B/%Y').strftime('%B/%d/%Y')
            #print (mydate)
        mydate = datetime.datetime.strptime(mydate, '%B/%d/%Y')
        PND["timestamp"] = PND["Hora"].apply(lambda x: mydate + datetime.timedelta(hours=int(x)))
        PND["tipo"] = "MTR"
        PND["sistema"] = sistema
        coleccionPND = coleccionPND.append(PND, ignore_index=True)
        PNDcount = PND.Hora.count()
        regcount = regcount + PNDcount

    coleccionPND.reset_index(drop=True)
    del coleccionPND["Derp"]
    # Export CSV or database
    ## dd/mm/yyyy format
    mydate = time.strftime("%d-%m-%Y")
    # Data integrity check for number of rows
    DataframetoimportSize = coleccionPND.Hora.count()
    if (DataframetoimportSize != regcount):
        print ('size check... PASSED')
        print ('Data Frame Size: %d'  % DataframetoimportSize)
        print ('Check Number: %d'  %  regcount)
        check = True
        #coleccionPND.to_csv('C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Download Data/CSVdir/PND/' + mydate + '.csv', index = False)
    if (DataframetoimportSize == regcount):
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
    global check

    getPNDpaths(MDA_path, MTR_path)
    uploadtoDB(pathlist_MDA, pathlist_MTR)
    if (check == True):
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