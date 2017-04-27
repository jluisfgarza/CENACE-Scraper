# -*- coding: utf-8 -*-
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
    # Save Path for system running the script
    save_path = "C:/Users/e-jlfloresg/Desktop/Python-Requests-CENACE/Cenace_Precios_Energia/Precios Marginales Locales/MDA/"
    #Today as DD-MM-YYYY
    d = "" + datetime.datetime.today().strftime("%d/%m/%Y")
    d = d.replace("/", "-")        
    """
    TESTING uncoment and comment top 2 lines
    d = "26-04-2017"
    """
    # SIN
    destino_pml_SIN = os.path.join(save_path, "PRUEBA" + "_SIN_PreciosMargLocalesMDA.csv")
    sec = 14
    microsec = 24    
    for sec in myrange: #[15]:
        for microsec in myrange: #[25]:
            for tzinfo in myrange: #[0, 1, 2, 3, 4, 5, 6, 7]:
                s = str(sec)
                m = str(microsec)
                t = str(tzinfo)
                if sec < 10:
                    s = "0"+s
                if microsec < 10:
                    m = "0"+m
                if tzinfo < 10:
                    t = "0"+t
                d2 = s + "-" + m + "-" + t
                # TESTING LOG print(d2)
                url_pml_SIN = "http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargLoc/MDA/Dia/5_" + d + "_" + d2 + "_SIN_PreciosMargLocalesMDA.csv"
                # TESTING LOG print(url_pml_SIN)
                a = requests.get(url_pml_SIN)
                if a.status_code == 404:
                    print ("ERROR 404")
                else:
                    print("Success")
                    pml_file = download_file(url_pml_SIN, destino_pml_SIN)
                    "break"
    # BCA
    print ("no se paro")

    # BCS
    print ("no se paro")
    
    return

"""
def getPML_MTR():
    return False

def getPND_MDA():
    return False

def getPND_MTR():
    return False
"""

#   Main Program
myrange = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
getPML_MDA()
"""
getPML_MTR()
getPND_MDA()
getPND_MTR()
"""
