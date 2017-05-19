from cx_Freeze import setup, Executable

setup(name = 'CenaceDownloader',
    version = '0.1',
    description ='Python Downloader: CENACE website for obtaining CSV files Site: ',
    executables = [Executable('Webdriver_Downloader.py')])
