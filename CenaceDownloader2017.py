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
    #TESTING uncoment and comment top 2 lines d = "02-05-2017"

    # SIN
    destino_pml_SIN = os.path.join(save_path, "PRUEBA" + "_SIN_PreciosMargLocalesMDA.csv")
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
                d2 = h + "-" + m + "-" + s
                # TESTING LOG
                print(d2)
                url_pml_SIN = "http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargLoc/MDA/Dia/5_" + d + "_" + d2 + "_SIN_PreciosMargLocalesMDA.csv"
                # TESTING LOG print(url_pml_SIN)
                a = requests.get(url_pml_SIN)
                if a.status_code == 404:
                    print ("ERROR 404")
                else:
                    print("Success")
                    pml_file = download_file(url_pml_SIN, destino_pml_SIN)
                    return True

    # BCA
    destino_pml_BCA = os.path.join(save_path, "PRUEBA" + "_BCA_PreciosMargLocalesMDA.csv")
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
                d2 = h + "-" + m + "-" + s
                # TESTING LOG print(d2)
                url_pml_BCA = "http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargLoc/MDA/Dia/5_" + d + "_" + d2 + "_BCA_PreciosMargLocalesMDA.csv"
                # TESTING LOG print(url_pml_BCA)
                a = requests.get(url_pml_BCA)
                if a.status_code == 404:
                    print ("ERROR 404")
                else:
                    print("Success")
                    pml_file = download_file(url_pml_BCA, destino_pml_BCA)
                    return True
    # BCS
    destino_pml_BCS = os.path.join(save_path, "PRUEBA" + "_BCS_PreciosMargLocalesMDA.csv")
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
                d2 = h + "-" + m + "-" + s
                # TESTING LOG print(d2)
                url_pml_BCS = "http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargLoc/MDA/Dia/5_" + d + "_" + d2 + "_BCS_PreciosMargLocalesMDA.csv"
                # TESTING LOG print(url_pml_BCS)
                a = requests.get(url_pml_BCS)
                if a.status_code == 404:
                    print ("ERROR 404")
                else:
                    print("Success")
                    pml_file = download_file(url_pml_BCS, destino_pml_BCS)
                    return True
    return

def getPND_MDA():
    # Save Path for system running the script
    save_path = "C:/Users/e-jlfloresg/Desktop/Python-Requests-CENACE/Cenace_Precios_Energia/Precios de Nodos Distribuidos/MDA"
    #Today as DD-MM-YYYY
    """
    d = "" + datetime.datetime.today().strftime("%d/%m/%Y")
    d = d.replace("/", "-")
    """
    #TESTING uncoment and comment top 2 lines
    d = "02-05-2017"
    # SIN
    destino_pnd_SIN = os.path.join(save_path, "PRUEBA" + "_SIN_PreciosNodosDistribuidosMDA.csv")
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
                d2 = h + "-" + m + "-" + s
                # TESTING LOG
                print(d2)
                url_pnd_SIN = "http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargReg/MDA/Dia/26_" + d + "_" + d2 + "_SIN_PreciosNodosDistribuidosMDA.csv"
                # TESTING LOG print(url_pnd_SIN)
                a = requests.get(url_pnd_SIN)
                if a.status_code == 404:
                    print ("ERROR 404")
                else:
                    print("Success")
                    pnd_file = download_file(url_pnd_SIN, destino_pnd_SIN)
                    return True

    # BCA
    destino_pnd_BCA = os.path.join(save_path, "PRUEBA" + "_BCA_PreciosNodosDistribuidosMDA.csv")
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
                d2 = h + "-" + m + "-" + s
                # TESTING LOG
                print(d2)
                url_pnd_BCA = "http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargReg/MDA/Dia/26_" + d + "_" + d2 + "_BCA_PreciosNodosDistribuidosMDA.csv"
                # TESTING LOG print(url_pnd_BCA)
                a = requests.get(url_pnd_BCA)
                if a.status_code == 404:
                    print ("ERROR 404")
                else:
                    print("Success")
                    pnd_file = download_file(url_pnd_BCA, destino_pnd_BCA)
                    return True
    # BCS
    destino_pnd_BCS = os.path.join(save_path, "PRUEBA" + "_BCS_PreciosNodosDistribuidosMDA.csv")
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
                d2 = h + "-" + m + "-" + s
                # TESTING LOG
                print(d2)
                url_pnd_BCS = "http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargReg/MDA/Dia/26_" + d + "_" + d2 + "_BCS_PreciosNodosDistribuidosMDA.csv"
                # TESTING LOG print(url_pnd_BCS)
                a = requests.get(url_pnd_BCS)
                if a.status_code == 404:
                    print ("ERROR 404")
                else:
                    print("Success")
                    pnd_file = download_file(url_pnd_BCS, destino_pnd_BCS)
                    return True

def getPML_MTR():
    #http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargLoc/MTR/Dia/PreciosMargLocales SIN MTR_Expost Dia 2017-04-26 v2017 05 02_15 36 14.csv
    return False

#def getPND_MTR():
#    return False

#   Main Program
myrange = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]

#getPML_MDA()
getPND_MDA()
#getPML_MTR()
#getPND_MTR()
