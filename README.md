# Python-Requests-CENACE

Python Downloader: CENACE website downloader for obtaining CSV files (Mexico). These files are processed and uploaded to a SQL server where data could be analyzed.

Site: [CENACE](http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx)


### Description
1. Files are downloaded by the `webdriver` script and read on the `CSVdir` directory by the daily scripts.
2. Daily Scripts connect to the azure server and upload information for data analysis.


### Scripts
`Pandas_PML_Daily.py` and `Pandas_PND_Daily.py` : Parse information downloaded from CENACE to the SQL Database every day.

`Pandas_PML_Monthly.py` and `Pandas_PND_Monthly.py` : Initialize the sql database with past information from CENACE.


## Installation
To use the tool, it is necessary to download and install:
-  [Geckodriver](https://github.com/mozilla/geckodriver/releases)
-  [Firefox](https://www.mozilla.org/en-US/firefox/new/)
-  [Python  3.6.0+](https://www.python.org/downloads/)

> **Note:**
> - To install Geckodriver in windows it is necessary to add geckodriver.exe to the systems path  


## Current Working Functions
- [x] Enter [CENACE](http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx) and download files to the specified directory
- [x] Validate downloads
- [x] Use Pandas lib to parse CSV files on specified directory
- [x] Create a daily condensed CSV files for PML and PND
- [x] Validate data integrity as dataframe
- [x] Local DB Connection
- [x] Local DB INSERT and SELECT

## Pending
- [ ] Finish monthly scripts
- [ ] Azure DB connection
- [ ] Azure data upload
- [ ] Initialize DB with past information using monthly scripts
- [ ] Run every 24 hrs
- [ ] Performance

## Performance
current code performance with large amounts of data is slow.
About 165,000 inserts per min on a system with:
  - AMD A8-5550M APU 2.10 Ghz
  - 8 GB RAM
  - 64bit OS

Further testing to be made.
> According to code logic, performance is due to `to_sql` function on pandas lib.


## Download (CSVdir) and Backup Directories tree view (PartCSVBackup)
```
  PML
    MDA
    MTR
  PND
    MDA
    MTR
```

> Don't forget to change the download paths!!

 Example on file Webdriver_Downloader:
``` python
profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Requests-CENACE\SELENIUM\test downloads\PML\MTR")
```
