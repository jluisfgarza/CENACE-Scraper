# Authors:
#    Fransisco Con Garza
#    Ricardo Alatorre Cantú
#    Juan Luis Flores Garza
# Date: 6/21/2017
#
# Downloader for PML - (Precios Marginales Locales)

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
MDA_path = "C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Download Data/CSVdir/PML/MDA/"
MTR_path = "C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Download Data/CSVdir/PML/MTR/"
coleccionPML = pd.DataFrame()

def getPMLpaths(dir1, dir2):
    global pathlist_MDA

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

    #MDA
    for element in pathlist1:
        path = element
        print(path + '\n')
        if path.find('_SIN_PreciosMargLocalesMDA') >= 0:
            sistema = 'SIN'
        if path.find('_BCA_PreciosMargLocalesMDA') >= 0:
            sistema = 'BCA'
        if path.find('_BCS_PreciosMargLocalesMDA') >= 0:
            sistema = 'BCS'
        PML = pd.read_csv(path, skiprows=[0,1,2,3,4,5,6])
        # Init Columns
        PML.columns = ["Hora","Nodo","Precio","Energía","Pérdidas","Congestión"]
        # Get the date from CSV header
        fecha = pd.read_csv(path, nrows=1, skiprows=[0,1,2])
        locale.setlocale(locale.LC_TIME, 'es')
        alfa = fecha["Reporte diario"].to_string(index=False)
        # Get substr with the date and format it
            #print(fecha)
        mydate = datetime.datetime.strptime(alfa[-len(alfa)+alfa.index(" ")+1:], '%d/%B/%Y').strftime('%B/%d/%Y')
            #print (mydate)
        mydate = datetime.datetime.strptime(mydate, '%B/%d/%Y')
        PML["timestamp"] = PML["Hora"].apply(lambda x: mydate + datetime.timedelta(hours=int(x)))
        PML["tipo"] = "MDA"
        PML["sistema"] = sistema
        coleccionPML = coleccionPML.append(PML, ignore_index=True)

    #MTR
    for element in pathlist2:
        path = element
        print(path + '\n')
        if path.find('PreciosMargLocales SIN MTR_') >= 0:
            sistema = 'SIN'
        if path.find('PreciosMargLocales BCA MTR_') >= 0:
            sistema = 'BCA'
        if path.find('PreciosMargLocales BCS MTR_') >= 0:
            sistema = 'BCS'
        PML = pd.read_csv(path, skiprows=[0,1,2,3,4,5,6])
        # Init Columns
        PML.columns = ["Hora","Nodo","Precio","Energía","Pérdidas","Congestión"]
        # Get the date from CSV header
        fecha = pd.read_csv(path, nrows=1, skiprows=[0,1,2])
        locale.setlocale(locale.LC_TIME, 'es')
        alfa = fecha["Reporte diario"].to_string(index=False)
        # Get substr with the date and format it
            #print(fecha)
        mydate = datetime.datetime.strptime(alfa[-len(alfa)+alfa.index(" ")+1:], '%d/%B/%Y').strftime('%B/%d/%Y')
            #print (mydate)
        mydate = datetime.datetime.strptime(mydate, '%B/%d/%Y')
        PML["timestamp"] = PML["Hora"].apply(lambda x: mydate + datetime.timedelta(hours=int(x)))
        PML["tipo"] = "MTR"
        PML["sistema"] = sistema
        coleccionPML = coleccionPML.append(PML, ignore_index=True)

    coleccionPML.reset_index(drop=True)
    # Export CSV or database
    ## dd/mm/yyyy format
    mydate = time.strftime("%d-%m-%Y")
    coleccionPML.to_csv('C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Download Data/CSVdir/PML/' + mydate + '.csv', index = False)

    return

################################# Main Program ################################
getPMLpaths(MDA_path, MTR_path)
uploadtoDB(pathlist_MDA, pathlist_MTR)
