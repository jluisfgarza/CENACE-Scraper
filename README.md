# Python-Requests-CENACE

Python Downloader: CENACE website downloader for obtaining CSV files (Mexico). These files are processed and uploaded to a SQL server where data could be analyzed.

Site: [CENACE](http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx)


### Description
1. Files are downloaded by the `PythonWebScrapper.py` script.
2. Files are read by the `DailyScirpts` on the `CSVdir`, then they are INSERTED on the SQL DB.

### Scripts
`Pandas_PML_Daily.py` and `Pandas_PND_Daily.py` : Parse information downloaded from CENACE to the SQL Database every day.

`Pandas_PML_Monthly.py` and `Pandas_PND_Monthly.py` : INSERT to the SQL database historical data from CENACE.


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
- [x] PML monthly script
- [x] PND monthly script
- [x] PML daily script
- [x] PND daily script

## Pending
- [ ] Azure DB connection
- [ ] Azure data upload
- [ ] Initialize DB with past information using monthly scripts
- [ ] Run every 24 hrs
- [ ] Performance

## Performance
current code performance with large amounts of data is slow.
About 165,000 inserts per min on a system with:
  - AMD A8-5550M APU 2.10 Ghz
    - CPU load when INSERT historical data ~(40%-55%)
    >  Working laptop with common programs and bloat ware running (Lotus, IBM, CITRIX, McAfee, Atom Editor, Spiyder, SQL Server Management Studio, etc.)

  - 8 GB RAM when INSERT historical data
    -   Memory ~(35%-45%)
    > Running SQL Server Windows NT 64bit, python and Spyder as main processes, the python process tend to consume different amounts of memory due to the file size variability.

  - 64bit Windows 8 OS


Further testing to be made.
> According to code logic, performance bottle neck is due to `to_sql` function on pandas lib.

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
