# -*- coding: utf-8 -*-
"""
Precios Marginales Locales

"""

import pandas as pd
import os
import datetime
import time
import locale

#coleccion = pd.read_pickle("PML.pkl")

coleccion = pd.DataFrame()

pathlist_POST = []
for subdir, dirs, files in os.walk('C:/Users/RALATORRE/Desktop/Bases de datos de mercado mayorista/PND/MTR/BCS/Post-Cambio/'):
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

coleccion.reset_index(drop=True)
del coleccion["Derp"]
del coleccion["Hora"]

coleccion.to_csv('C:/Users/RALATORRE/Desktop/Bases de datos de mercado mayorista/PND/MTR/BCS/PND-MTR-BCS.csv', index = False)
