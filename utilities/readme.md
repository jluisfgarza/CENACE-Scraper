# Cenace Gráfica de Demanda

### Update
Server side app blocks requests, requests must be done on the browser console while in being on `http://www.cenace.gob.mx/`

[Grafica Demanda sitio](http://www.cenace.gob.mx/GraficaDemanda.aspx)
 - request url http://www.cenace.gob.mx/ajax.aspx
 - realtime every 5min

### Ajax Requests per Region
 [JS Demanda](http://www.cenace.gob.mx/scripts/funcionesIndex.js) Sistema Eléctrico Nacional / Region

###### Sample Request success for every region
```
/ajax.aspx
VM9067:11 2,010 MW&1,966 MW&353 MW&289 MW&7,408 MW&5,017 MW&8,139 MW&11,352 MW&3,446 MW&2,995 MW&4,096 MW&2,994 MW&8,464 MW&6,600 MW&5,368 MW&9,093 MW&1,747 MW&750 MW&40,870 MW&38,668 MW&38,802 MW&30/06/2017 11:40:18 AM&viernes 30 junio 2017&39,076 MW&1,906 MW&312 MW&7,276 MW&7,665 MW&3,280 MW&4,151 MW&8,291 MW&5,947 MW&1,743 MW&Friday June 30 2017
```
| Region              | BC | BCS | CEN | NE | NO | NTE | OCC | OR | PEN | NACNeta |   |   |
|---------------------|----|-----|-----|----|----|-----|-----|----|-----|---------|---|---|
| Demanda             | 0  | 2   | 4   | 6  | 8  | 10  | 12  | 14 | 16  | 19      |   |   |
| Generación          | 1  | 3   | 5   | 7  | 8  | 11  | 13  | 15 | 17  | 20      |   |   |
| Enlace (Pronóstico) | 24 | 25  | 26  | 27 | 28 | 29  | 30  | 31 | 32  | 23      |   |   |

 Check formatted testAjaxRequests.html

### Ajax Requests per Hour
[JS Demanda Desgloce por hora](http://www.cenace.gob.mx/scripts/funcionesGrafica.js)
###### Request sistema interconectado nacional
```
$.ajax({
            type: "post",
            url: "GraficaDemanda.aspx/obtieneValoresTotal",
            data: '{"gerencia":"10"}',
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function (response) {
                chartData = [];
                chart.dataProvider = chartData;
                valorMaxPronosticoDA = 0;
                valorMax = 0;
                if (response.d == "") {
                    setTimeout(cargaGrafica, 5000, '10');
                    return;
                }
                response.d = $.parseJSON(response.d);
				console.log(response)                
            }
        });
```
###### Sample Request success per hour for SIN
```
Object {d: Array(24)}
 d:Array(24)
  0:Object
    hora:"1"
    valorDemanda:"36881"
    valorEnlace:null
    valorGeneracion:"36689"
    valorPronostico:"37238"
    __proto__:Object
  1:Object
    hora:"2"
    valorDemanda:"35650"
    valorEnlace:null
    valorGeneracion:"35456"
    valorPronostico:"35905"
    __proto__:Object
  2:Object
  .
  .
  .
  23:Object
```
Check formatted testAjaxRequests2.html
