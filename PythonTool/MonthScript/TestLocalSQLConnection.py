# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 11:25:04 2017

@author: e-jlfloresg
"""

import pandas as pd
import sqlalchemy as sa
import pyodbc

# Local DB 
engine = sa.create_engine('mssql+pyodbc://E-JLFLORESG/PreciosEnergía?driver=SQL+Server+Native+Client+11.0')

with engine.connect() as conn, conn.begin():
    # pending change DB name 
    # SQl query read top 10 rows on PML db
    PML = pd.read_sql('SELECT TOP (10) [Hora], [Nodo], [Precio], [Energia], [Perdidas], [Congestion], [timestamp] FROM [PreciosEnergía].[dbo].[PML]', conn)
    print (PML)
    # SQl query read top 10 rows on PML db
    PND = pd.read_sql('SELECT TOP (10) [Hora], [Zona de Carga], [Precio Zonal], [Energia], [Perdidas], [Congestion], [timestamp] FROM [PreciosEnergía].[dbo].[PND]', conn)
    print (PND)