# -*- coding: utf-8 -*-
import csv
import requests
import datetime
import os.path
"""
import os.path -> Save file to cutom path
save_path = "C:/Users/User/My_Path/Precios de la Energía/"
The next 2 paths are predefined in the script:
- Precios Marginales Locales/MTR/Diarios/ + Mes
- Precios Nodos Distribuidos/MTR/Diarios/ + Mes

Notes:
    Custom Downloader CENACE 2017
    Request Paths (Precios Diarios):
        GLobal path: http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/
            PML:  MargLoc/
            MTR: MTR/Dia/
                    SISTEMA INTERCONECTADO NACIONAL
                        - PreciosMargLocales%20SIN%20MTR_Expost%20Dia%202017-04-18%20v2017%2004%2024_14%2055%2022.csv
                    SISTEMA INTERCONECTADO BAJA CALIFORNIA
                        - PreciosMargLocales%20BCA%20MTR_Expost%20Dia%202017-04-18%20v2017%2004%2024_12%2053%2001.csv
                    SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR
                        - PreciosMargLocales%20BCS%20MTR_Expost%20Dia%202017-04-18%20v2017%2004%2024_14%2054%2036.csv
            PND: MargReg/
                MTR: MTR/Dia/
                    SISTEMA INTERCONECTADO NACIONAL
                        - PreciosNodosDistrib%20SIN%20MTR_Expost%20Dia%202017-04-18%20v2017%2004%2024_14%2055%2022.csv
                    SISTEMA INTERCONECTADO BAJA CALIFORNIA
                        - PreciosNodosDistrib%20BCA%20MTR_Expost%20Dia%202017-04-18%20v2017%2004%2024_12%2053%2001.csv
                    SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR
                        - PreciosNodosDistrib%20BCS%20MTR_Expost%20Dia%202017-04-18%20v2017%2004%2024_14%2054%2036.csv
"""

# Global Variables
#Today as DD-MM-YYYY
"""
dd2 = "" + datetime.datetime.today().strftime("%Y/%m/%d")
dd2 = d.replace("/", "-")
"""
#TESTING uncoment and comment top 2 lines
dd2 = "2017-04-26"
year = d[:4]
MTR_SIN_d2 = ""
MTR_BCA_d2 = ""
MTR_BCS_d2 = ""

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

def getPML_MTR():
    #SIN http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargLoc/MTR/Dia/PreciosMargLocales%20SIN%20MTR_Expost%20Dia%202017-04-26%20v2017%2005%2002_15%2036%2014.csv
        #http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargLoc/MTR/Dia/PreciosMargLocales SIN MTR_Expost Dia 2017-04-26 v2017 05 02_15 36 14.csv
    destino_pml_SIN = os.path.join(save_path, "PRUEBA" + "_SIN_PreciosMargLocalesMTR.csv")
    # [15] [09] myrange
    for hour in myrange:
        for minute in myrange:
            for second in myrange:
                h = str(hour)
                m = str(minute)
                s = str(second)
                if hour < 10:
                    h = "0"+h
                if minute < 10:
                    m = "0"+m
                if second < 10:
                    s = "0"+s
                global MDA_SIN_d2
                MDA_SIN_d2 = h + "-" + m + "-" + s
                # TESTING LOG print(MDA_SIN_d2)
                # TESTING LOG print(d)
                url_pml_SIN = "http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargLoc/MTR/Dia/PreciosMargLocales SIN MTR_Expost Dia " + dd2 + " V " + year + MDA_SIN_d2 + "_SIN_PreciosMargLocalesMTR.csv"
                # TESTING LOG print(url_pml_SIN)
                a = requests.get(url_pml_SIN)
                if a.status_code == 404:
                    print ("ERROR 404")
                else:
                    print("Success")
                    # TESTING LOG print(url_pml_SIN)
                    pml_file = download_file(url_pml_SIN, destino_pml_SIN)
                    return True

    #BCA http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargLoc/MTR/Dia/PreciosMargLocales%20BCA%20MTR_Expost%20Dia%202017-04-26%20v2017%2005%2002_13%2028%2036.csv

    #BCS http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargLoc/MTR/Dia/PreciosMargLocales%20BCS%20MTR_Expost%20Dia%202017-04-26%20v2017%2005%2002_15%2033%2030.csv

    return

def getPND_MTR():

    #SIN http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargReg/MTR/Dia/PreciosNodosDistrib%20SIN%20MTR_Expost%20Dia%202017-04-26%20v2017%2005%2002_15%2036%2014.csv

    #BCA http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargReg/MTR/Dia/PreciosNodosDistrib%20BCA%20MTR_Expost%20Dia%202017-04-26%20v2017%2005%2002_13%2028%2036.csv

    #BCS http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargReg/MTR/Dia/PreciosNodosDistrib%20BCS%20MTR_Expost%20Dia%202017-04-26%20v2017%2005%2002_15%2033%2030.csv

    return

# Main Program
myrange = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
getPML_MTR()
getPND_MTR()
