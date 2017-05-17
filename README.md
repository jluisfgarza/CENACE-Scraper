Python-Requests-CENACE
===================

Python Downloader: CENACE website for obtaining CSV files
Site: http://www.cenace.gob.mx/SIM/VISTA/REPORTES/PreEnergiaSisMEM.aspx

----------

Instalación
-------------

Para utilizar el script es necesario descargar la versión más reciente de:

-  [Geckodriver](https://github.com/mozilla/geckodriver/releases)
-  [Firefox](https://www.mozilla.org/es-MX/firefox/new/)
-  [Python  3.6.0+](https://www.python.org/downloads/)

> **Nota:**

> - Para instalar geckodriver en windows fué necesario agregar al path  del .exe a la variable de sistema PATH

----------


Funcionalidades Pendientes
-------------

- Revisar 12 descargas correctas
- Ejecutción automática cada 24 hrs

----------
Downloader Tree
-------------

PML
:   MDA
:   MTR

PND
:   MDA
:   MTR

	> Se debe definir el path de descarga nuevamente para cada ordenador donde se corra el script.
> ```
profile.set_preference("browser.download.dir", "C:\\Users\e-jlfloresg\Desktop\Python-Requests-CENACE\SELENIUM\test downloads\PML\MTR")
```
