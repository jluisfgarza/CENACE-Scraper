from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

# Google Chorme
path = "C:/Users/e-jlfloresg/SELENIUM/chromedriver_win32/chromedriver.exe"
browser = webdriver.Chrome(path)  # Optional argument, if not specified will search path.

# Internet Explorer                         
#path = "C:/Users/e-jlfloresg/SELENIUM/IEDriverServer.exe"
#browser = webdriver.Ie(path)  # Optional argument, if not specified will search path.

def checkboxes():
    #PML/MDA/D
    searchcheckbox("4")
    #PML/MTR/D
    searchcheckbox("3")
    #PND/MDA/D
    #searchcheckbox("5")
    #PND/MTR/D
    #searchcheckbox("5")
    return
                       
def checktable():    
    try:
        browser.find_element_by_xpath("(//SPAN[@class='rtUnchecked'])[1]")         
        return True              
    except NoSuchElementException:        
        print("Error Tabla")                        
        return False

def searchcheckbox(strindex): 
    try:
        browser.find_element_by_xpath("(//SPAN[@class='rtUnchecked'])[" + strindex + "]").click() 
        return
    except NoSuchElementException as e:
        print("Error finding the element")
        time.sleep(1)        
    return      

### Main Program ###
browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')
time.sleep(3)

for i in range(1,6):
    if (checktable() == False):        
        browser.refresh()        
        time.sleep(10)
    else:
        checkboxes()

        
    