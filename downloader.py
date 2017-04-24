# -*- coding: utf-8 -*-
"""
Descarga de archivos de precios marginales MEM
"""

import csv
import requests
import datetime

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

#conexos------------------------

#check for existing dates
#daterangestart = datetime.datetime(2016,9,6,15,31,00)
daterangestart = datetime.datetime(2017,01,01,00,00,00)
increment = datetime.timedelta(0,1)
daterange = range(60*1*1)
d = daterangestart

for intento in daterange:
    #datestamp = "18-04-2016_13-58-51"
    d = d+increment
    # days 01,02,03....12,13...31
    if d.day >10:
        strday = str(d.day)
    else:
        strday = "0"+str(d.day)
    # months 01,02,03....12,
    if d.month >10:
        strmonth = str(d.month)
    else:
        strmonth = "0"+str(d.month)
    stryear = str(d.year)
    # hours 01,02,03....12
    if d.hour >10:
        strhour = str(d.hour)
    else:
        strday = "0"+str(d.hour)
    # minute 01,02,03....12,13...59
    if d.minute >10:
        strminute = str(d.minute)
    else:
        strminute = "0"+str(d.minute)
    # second 01,02,03....12,13...59
    if d.second >=10:
        strsecond = str(d.second)
    else:
        strsecond = "0"+str(d.second)
    cenacedatestamp = strday+"-"+strmonth+"-"+stryear+"_"+strhour+"-"+strminute+"-"+strsecond
    print("using datestamp: "+cenacedatestamp)
    url_pml = "http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargLoc/MDA/Dia/5_"+cenacedatestamp+"_SIN_PreciosMargLocalesMDA.csv"
    #url_conexos = "http://www.cenace.gob.mx/DocsMEM/OpeMdo/ServConx/MDA/Dia/34_"+cenacedatestamp+"_SIN_PreciosServiciosConexosMDA.csv"
    destino_pml = "PML-"+cenacedatestamp+".csv"
    #destino_conexos = "CON-"+cenacedatestamp+".csv"
    a = requests.get(url_pml)
    if a.status_code == 404:
        print ("ERROR 404")
    else:
        print("Success")
        pml_file = download_file(url_pml,destino_pml)
        break



#Precios Marginales locales
#http://www.cenace.gob.mx/DocsMEM/OpeMdo/PreEner/MargLoc/MDA/Dia/5_20-04-2016_13-31-40_SIN_PreciosMargLocalesMDA.csv
