from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
    browser.refresh()
    loadsite()
    return

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
                       
def searchcheckbox(mychar): 
    try:
        browser.find_element_by_xpath("(//SPAN[@class='rtUnchecked'])[" + mychar + "]").click() 
        return
    except NoSuchElementException as e:
        print("Error finding the element")
    return      

### Main Program ###

# Google Chorme
path = "C:/Users/e-jlfloresg/SELENIUM/chromedriver_win32/chromedriver.exe"
browser = webdriver.Chrome(path)  # Optional argument, if not specified will search path.
browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
delay = 15 #seconds
loadsite()

        
    