from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

path = "C:/Users/e-jlfloresg/SELENIUM/chromedriver_win32/chromedriver.exe"
browser = webdriver.Chrome(path)  # Optional argument, if not specified will search path.
browser.get('http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx')

for i in range(50):
    try:
        browser.find.element_by_xpath(".//*[contains(text(),'Precios de la energía')]").click()
        break
    except NoSuchElementException as e:
        print("rety")
        time.sleep(1)
else:
    print ("test failed")
