# Download files

Files are downloaded and read on the `CSVdir` directory.

### Download Dir (CSVdir)
```
PML
  MDA
  MTR
PND
  MDA
  MTR
```

### Scripts
Pandas_PML_Daily and Pandas_PND_Daily are prepared to parse information downloaded from CENACE to the SQL Database every day.

Pandas_PML_Monthly and Pandas_PND_Monthly where used to initialize the sql database with past information from CENACE. These scripts are prepared to fix possible header differences among files and process the CSV files that contain information of 1/2 a month at a time.

> Don't forget to change the download paths!!

> Example on file Webdriver_Downloader:
``` python
profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Requests-CENACE\SELENIUM\test downloads\PML\MTR")
```
