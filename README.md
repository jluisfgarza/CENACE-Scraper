Python-Requests-CENACE
===================

Python Downloader: CENACE website downloader for obtaining CSV files (Mexico)
Site: http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx
-------------

## Installation
To use the tool, it is necessary to download and install:
-  [Geckodriver](https://github.com/mozilla/geckodriver/releases)
-  [Firefox](https://www.mozilla.org/en-US/firefox/new/)
-  [Python  3.6.0+](https://www.python.org/downloads/)

> **Note:**
> - To install Geckodriver in windows it is necessary to add geckodriver.exe to the systems path  

-------------

## Pending
- [ ] Validate 12 downloads
- [ ] Run every 24 hrs.
-------------

## Downloader Tree
```
PML
  MDA
  MTR
PND
  MDA
  MTR
```
-------------

> Don't forget to change the download path!!

``` python
profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Requests-CENACE\SELENIUM\test downloads\PML\MTR")
```
