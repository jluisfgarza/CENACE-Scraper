from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.useDownloadDir", False)
profile.set_preference("browser.download.downloadDir", 'C:/Users/e-jlfloresg/Desktop/Python-Requests-CENACE/SELENIUM/test downloads')
#profile.set_preference("browser.helperApps.alwaysAsk.force", False)
profile.set_preference('browser.helperApps.neverAsk.openFile', ('application/octet-stream, ')) 
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/octet-stream,'))
browser = webdriver.Firefox(firefox_profile=profile)
browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
delay = 15 #seconds

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

def downloadfiles(  ):
    time.sleep(10);
    try:
        browser.find_element_by_xpath("//*[@id=\"ctl00_ContentPlaceHolder1_ListViewNodos_ctrl0_ListViewArchivosSIN_ctrl0_linkCSV\"]").click()    
        return
    except NoSuchElementException as e:
        print("Error no encontre csv")
    return

### Main Program ###
loadsite()
downloadfiles()
#webdriver.close()
#browser.close()