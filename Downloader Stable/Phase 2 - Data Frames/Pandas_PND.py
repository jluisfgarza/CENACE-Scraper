# Authors:
#    Fransisco Con Garza
#    Ricardo Alatorre Cantú
#    Juan Luis Flores Garza
# Date: 5/17/2017
#
# Downloader for PND - (Precios Nodos Distribuidos)

import pandas as pd
import os
import datetime
import time
import locale

def getDataPND(mypath, ElectricSys):
    coleccion = pd.DataFrame()
    pathlist_POST = []

    for subdir, dirs, files in os.walk(mypath):
        for file in files:
            filepath = subdir + os.sep + file

            if filepath.endswith(".csv"):
                path = filepath
                pathlist_POST.append(path)

    for element in pathlist_POST:
        path = element
        PML = pd.read_csv(path, skiprows=[0,1,2,3,4,5,6])
        PML.columns = ["Hora","Zona de Carga","Precio Zonal","Energía","Pérdidas","Congestión", "Derp"]
        fecha = pd.read_csv(path, nrows=1, skiprows=[0,1,2])
        locale.setlocale(locale.LC_TIME, 'es')
        alfa = fecha["Reporte diario"].to_string(index=False)
        PML["timestamp"] = PML["Hora"].apply(lambda x: datetime.datetime.strptime(alfa[-len(alfa)+alfa.index(" ")+1:], "%d/%B/%Y") + datetime.timedelta(hours=int(x)))
        coleccion = coleccion.append(PML, ignore_index=True)

    #Delete columns
    coleccion.reset_index(drop=True)
    del coleccion["Derp"]
    del coleccion["Hora"]
    return # End getDataPND()

coleccion.to_csv('C:/Users/RALATORRE/Desktop/Bases de datos de mercado mayorista/PND/MTR/BCS/PND-MTR-BCS.csv', index = False)


################################# Main Program #################################
'''
## MDA
### SISTEMA INTERCONECTADO NACIONAL
getDataPND("C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Phase 2 - Data Frames/test csv/PML/MDA", "SIN")
### SISTEMA INTERCONECTADO BAJA CALIFORNIA
getDataPND("C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Phase 2 - Data Frames/test csv/PML/MDA", "BCA")
### SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR
getDataPND("C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Phase 2 - Data Frames/test csv/PML/MDA", "BCS")

## MTR
### SISTEMA INTERCONECTADO NACIONAL
getDataPND("C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Phase 2 - Data Frames/test csv/PML/MTR", "SIN")
### SISTEMA INTERCONECTADO BAJA CALIFORNIA
getDataPND("C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Phase 2 - Data Frames/test csv/PML/MTR", "BCA")
### SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR
getDataPND("C:/Users/e-jlfloresg/Desktop/Python-Downloader-CENACE/Downloader Stable/Phase 2 - Data Frames/test csv/PML/MTR", "BCS")
'''
