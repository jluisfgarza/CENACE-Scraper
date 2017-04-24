# -*- coding: utf-8 -*-
"""
Notes:
    Custom Downloader CENACE 2017
    Request Paths (Precios Diarios):   
        GLobal path: http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/
            PML:  MargLoc/
                MDA : MDA/Dia/
                    SISTEMA INTERCONECTADO NACIONAL
                        - 5_24-04-2017_14-19-57_SIN_PreciosMargLocalesMDA.csv
                    SISTEMA INTERCONECTADO BAJA CALIFORNIA 
                        - 5_24-04-2017_12-03-59_BCA_PreciosMargLocalesMDA.csv
                    SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR 
                        - 5_24-04-2017_14-11-58_BCS_PreciosMargLocalesMDA.csv
                MTR
                    SISTEMA INTERCONECTADO NACIONAL
                        - PreciosMargLocales%20SIN%20MTR_Expost%20Dia%202017-04-18%20v2017%2004%2024_14%2055%2022.csv
                    SISTEMA INTERCONECTADO BAJA CALIFORNIA 
                        - PreciosMargLocales%20BCA%20MTR_Expost%20Dia%202017-04-18%20v2017%2004%2024_12%2053%2001.csv
                    SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR 
                        - PreciosMargLocales%20BCS%20MTR_Expost%20Dia%202017-04-18%20v2017%2004%2024_14%2054%2036.csv
            PND: MargReg/
                MDA: MDA/Dia/
                    SISTEMA INTERCONECTADO NACIONAL
                        - 26_24-04-2017_14-19-57_SIN_PreciosNodosDistribuidosMDA.csv
                    SISTEMA INTERCONECTADO BAJA CALIFORNIA 
                        - 26_24-04-2017_12-03-59_BCA_PreciosNodosDistribuidosMDA.csv
                    SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR 
                        - 26_24-04-2017_14-11-58_BCS_PreciosNodosDistribuidosMDA.csv
                MTR: MTR/Dia/
                    SISTEMA INTERCONECTADO NACIONAL
                        - PreciosNodosDistrib%20SIN%20MTR_Expost%20Dia%202017-04-18%20v2017%2004%2024_14%2055%2022.csv
                    SISTEMA INTERCONECTADO BAJA CALIFORNIA 
                        - PreciosNodosDistrib%20BCA%20MTR_Expost%20Dia%202017-04-18%20v2017%2004%2024_12%2053%2001.csv
                    SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR 
                        - PreciosNodosDistrib%20BCS%20MTR_Expost%20Dia%202017-04-18%20v2017%2004%2024_14%2054%2036.csv
"""

import csv
import requests
import datetime
import os.path 
"""
import os.path -> Save file to cutom path
save_path = "C:/Users/User/My_Path/Precios de la Energía/"
    The next 4 paths are predefined in the script:
        - Precios Marginales Locales/MDA/Diarios/ + Mes
        - Precios Marginales Locales/MTR/Diarios/ + Mes
        - Precios Nodos Distribuidos/MDA/Diarios/ + Mes
        - Precios Nodos Distribuidos/MTR/Diarios/ + Mes
        
"""

def download_file(url, output_file, compressed=True):
    """
    compressed: enable response compression support
    """
    # NOTE the stream=True parameter. It enable a more optimized and buffer support for data loading.
    headers = {}
    if compressed:
        headers["Accept-Encoding"] = "gzip"

    r = requests.get(url, headers=headers, stream=True)

    with open(output_file, 'wb') as f: #open as block write.
        for chunk in r.iter_content(chunk_size=4096):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
        f.flush() #Afterall, force data flush into output file (optional)

    return output_file

   
def getPML_MDA():   
    save_path = "C:/Users/e-jlfloresg/Desktop/Precios de la Energía/Precios Marginales Locales/MTR/"
    url_pml = "http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargLoc/MTR/Dia/PreciosMargLocales SIN MTR_Expost Dia 2017-01-27 v2017 02 02_18 24 02.csv"
    destino_pml = os.path.join(save_path, "PML-MTR_Expost Dia 2017-01-27 v2017 02 02_18 24 02.csv")
    
    a = requests.get(url_pml)
    if a.status_code == 404:
        print ("ERROR 404")
    else:
        print("Success")
        pml_file = download_file(url_pml,destino_pml, save_path)
    return False

def getPML_MTR():    
    return False

def getPND_MDA():    
    return False

def getPND_MTR():    
    return False


#   Main Program

getPML_MDA()
getPML_MTR()
getPND_MDA()
getPND_MTR()

