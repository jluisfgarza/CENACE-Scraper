from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Load site
def loadsite() :
    try:
        element_present = EC.presence_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_treePrincipal'))
        WebDriverWait(browser, delay).until(element_present)
        print ("Page is ready!")
        checkboxes()
        return
    except TimeoutException:
        print ("Error Code 1: Error Cargando página")
    except ElementNotVisibleException as nv:
        print("Error Code 2: Error cargado la tabla")
    except ElementNotInteractableException as ni:
        print("Error Code 3: Error cargado la tabla")
    browser.refresh()
    loadsite()
    return

# Index of each checkbox
def checkboxes():
    time.sleep(5);
    #PML/MDA/D
    searchcheckbox('4')
    #PML/MTR/D
    searchcheckbox('3')
    #PND/MDA/D
    searchcheckbox('5')
    #PND/MTR/D
    searchcheckbox('5')
    return

# Click on checkboxes
def searchcheckbox(mychar):
    try:
        browser.find_element_by_xpath("(//SPAN[@class='rtUnchecked'])[" + mychar + "]").click()
        
        return
    except NoSuchElementException as e:
        print("Error finding the element")
        browser.refresh()
        loadsite()
        return

def downloadfiles(Xpath):
    time.sleep(10);
    try:
        browser.find_element_by_xpath(Xpath).click()    
        return
    except NoSuchElementException as e:
        print("Error no encontre csv")
    return

### Main Program ###

### Precios Marginales Locales
# MDA SISTEMA INTERCONECTADO NACIONAL
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Requests-CENACE\SELENIUM\test downloads\PML\MDA")
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values')) 
browser = webdriver.Firefox(firefox_profile=profile)
browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
delay = 15 #seconds
loadsite()
downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl0_ListViewArchivosSIN_ctrl0_linkCSV\"]")
time.sleep(60)
browser.quit()

# MDA SISTEMA INTERCONECTADO BAJA CALIFORNIA
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Requests-CENACE\SELENIUM\test downloads\PML\MDA")
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values')) 
browser = webdriver.Firefox(firefox_profile=profile)
browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
delay = 15 #seconds
loadsite()
downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl0_ListViewArchivosBCN_ctrl0_A1\"]")
time.sleep(60)
browser.quit()

# MDA SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Requests-CENACE\SELENIUM\test downloads\PML\MDA")
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values')) 
browser = webdriver.Firefox(firefox_profile=profile)
browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
delay = 15 #seconds
loadsite()
downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl0_ListViewArchivosBCS_ctrl0_A4\"]")
time.sleep(60)
browser.quit()

# MTR SISTEMA INTERCONECTADO NACIONAL
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Requests-CENACE\SELENIUM\test downloads\PML\MTR")
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values')) 
browser = webdriver.Firefox(firefox_profile=profile)
browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
delay = 15 #seconds
loadsite()
downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl1_ListViewArchivosSIN_ctrl0_linkCSV\"]")
time.sleep(60)
browser.quit()

# MTR SISTEMA INTERCONECTADO BAJA CALIFORNIA
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Requests-CENACE\SELENIUM\test downloads\PML\MTR")
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values')) 
browser = webdriver.Firefox(firefox_profile=profile)
browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
delay = 15 #seconds
loadsite()
downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl1_ListViewArchivosBCN_ctrl0_A1\"]")
time.sleep(60)
browser.quit()

# MTR SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Requests-CENACE\SELENIUM\test downloads\PML\MTR")
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values')) 
browser = webdriver.Firefox(firefox_profile=profile)
browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
delay = 15 #seconds
loadsite()
downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl1_ListViewArchivosBCS_ctrl0_A4\"]")
time.sleep(60)
browser.quit()

### Precios de Nodos Distribuidos
# MDA SISTEMA INTERCONECTADO NACIONAL
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Requests-CENACE\SELENIUM\test downloads\PND\MDA")
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values')) 
browser = webdriver.Firefox(firefox_profile=profile)
browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
delay = 15 #seconds
loadsite()
downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl2_ListViewArchivosSIN_ctrl0_linkCSV\"]")
time.sleep(60)
browser.quit()

# MDA SISTEMA INTERCONECTADO BAJA CALIFORNIA
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Requests-CENACE\SELENIUM\test downloads\PND\MDA")
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values')) 
browser = webdriver.Firefox(firefox_profile=profile)
browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
delay = 15 #seconds
loadsite()
downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl2_ListViewArchivosBCN_ctrl0_A1\"]")
time.sleep(60)
browser.quit()

# MDA SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Requests-CENACE\SELENIUM\test downloads\PND\MDA")
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values')) 
browser = webdriver.Firefox(firefox_profile=profile)
browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
delay = 15 #seconds
loadsite()
downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl2_ListViewArchivosBCS_ctrl0_A4\"]")
time.sleep(60)
browser.quit()

# MTR SISTEMA INTERCONECTADO NACIONAL
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Requests-CENACE\SELENIUM\test downloads\PND\MTR")
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values')) 
browser = webdriver.Firefox(firefox_profile=profile)
browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
delay = 15 #seconds
loadsite()
downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl3_ListViewArchivosSIN_ctrl0_linkCSV\"]")
time.sleep(60)
browser.quit()

# MTR SISTEMA INTERCONECTADO BAJA CALIFORNIA
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Requests-CENACE\SELENIUM\test downloads\PND\MTR")
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values')) 
browser = webdriver.Firefox(firefox_profile=profile)
browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
delay = 15 #seconds
loadsite()
downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl3_ListViewArchivosBCN_ctrl0_A1\"]")
time.sleep(60)
browser.quit()

# MTR SISTEMA INTERCONECTADO BAJA CALIFORNIA SUR
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Requests-CENACE\SELENIUM\test downloads\PND\MTR")
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream, text/plain, text/x-csv, text/plain, application/vnd.ms-excel, text/x-csv, application/csv, application/x-csv, text/csv, text/comma-separated-values, text/x-comma-separated-values, text/tab-separated-values')) 
browser = webdriver.Firefox(firefox_profile=profile)
browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
delay = 15 #seconds
loadsite()
downloadfiles("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl3_ListViewArchivosBCS_ctrl0_A4\"]")
time.sleep(60)
browser.quit()