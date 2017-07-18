# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 11:25:04 2017

@author: e-jlfloresg
"""

import pandas as pd
import sqlalchemy as sa
#import pyodbc

# Local DB 
engine = sa.create_engine('mssql+pyodbc://E-JLFLORESG/PreciosEnergia?driver=SQL+Server+Native+Client+11.0')

with engine.connect() as conn, conn.begin():    
        
    # SQl query count rows on PML
    PML = pd.read_sql('SELECT COUNT(*) as [NumRegPML] FROM [PreciosEnergia].[dbo].[PML]', conn)
    
    # SQl query count rows on PND
    PND = pd.read_sql('SELECT COUNT(*) as [NumRegPND] FROM [PreciosEnergia].[dbo].[PND]', conn)
        
    PML.reset_index(drop=True)
    PND.reset_index(drop=True)
    TPML = PML.iat[0,0]
    TPND = PND.iat[0,0]
    print ('NumRegPML: ')
    print (TPML)
    print ('NumRegPND: ')
    print (TPND)


