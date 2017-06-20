# Authors:
#    Fransisco Con Garza
#    Ricardo Alatorre Cantú
#    Juan Luis Flores Garza
# Date: 5/17/2017
#
# Downloader for PML - (Precios Marginales Locales)

import pandas as pd
import os
import datetime
import locale
import pyodbc

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

coleccion = pd.DataFrame()    
pathlist_MDA = []
pathlist_MTR = []
    
for subdir, dirs, files in os.walk('C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Download Data/CSVdir/PML'):
    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith("PreciosMargLocalesMDA.csv"):
            path = filepath
            pathlist_MDA.append(path)
        else if filepath.endswith(".csv") && filepath.startswith("PreciosMargLocales"):
            path = filepath
            pathlist_MTR.append(path)

for element in pathlist_POST:        
    path = element
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
    coleccion = coleccion.append(PML, ignore_index=True)

coleccion.reset_index(drop=True)

# Export CSV
coleccion.to_csv('C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Download Data/CSVdir/PML'+ tipo + esystem + '.csv', index = False)

################################# Main Program #################################
## MDA
### SISTEMA INTERCONECTADO NACIONAL
getDataPML('C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Download Data/CSVdir/PML/MDA/PreciosMargLocalesMDA.csv', 'MDA', 'SIN')
### SISTEMA INTERCONECTADO BAJA CALIFORNIA
getDataPML('C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Download Data/CSVdir/PML/MDA/PreciosMargLocalesMDA.csv', 'MDA', "BCA")
### SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR
getDataPML('C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Download Data/CSVdir/PML/MDA/PreciosMargLocalesMDA.csv', 'MDA', "BCS")

## MTR
### SISTEMA INTERCONECTADO NACIONAL
getDataPML("C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Phase 2 - Data Frames/test csv/PML/MTR", "SIN")
### SISTEMA INTERCONECTADO BAJA CALIFORNIA
getDataPML("C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Phase 2 - Data Frames/test csv/PML/MTR", "BCA")
### SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR
getDataPML("C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Phase 2 - Data Frames/test csv/PML/MTR", "BCS")
'''
