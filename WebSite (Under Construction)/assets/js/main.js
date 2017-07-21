/*
Hora
Clave del nodo
Precio marginal local ($/MWh)
Componente de energia ($/MWh)
Componente de perdidas ($/MWh)
Componente de congestion ($/MWh)
*/
var data = [];
var jasondata = [{}];

d3.queue()
    .defer(d3.csv, "test1.csv")
    .defer(d3.csv, "test2.csv")
    .await(analyze);

function analyze(error, test1, test2) {
    if (error) {
        console.log(error);
    }

    data = readfile(d3.merge([test1, test2]));
    jsondata = (JSON.stringify(data, null, "\t"));
    console.log(jsondata);
    //console.log(data);  

}

function readfile(data) {
    data.forEach(function (d) {
        temp = d["Fecha"];
        temp = temp + d["Hora"];
        temp = parseDate(temp);
        //console.log(Date.parse(temp));
        d["Fecha"] = temp,
        d["Hora"] = +d["Hora"],
        d["Clave del nodo"] = d["Clave del nodo"],
        d["Precio marginal local ($/MWh)"] = +d["Precio marginal local ($/MWh)"],
        d["Componente de energia ($/MWh)"] = +d["Componente de energia ($/MWh)"],
        d["Componente de perdidas ($/MWh)"] = +d["Componente de perdidas ($/MWh)"],
        d["Componente de congestion ($/MWh)"] = +d["Componente de congestion ($/MWh)"]
    })
    return (data);
};
