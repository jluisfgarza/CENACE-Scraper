d3.queue()
    .defer(d3.csv, "test1.csv")
    .defer(d3.csv, "test2.csv")
    .await(analyze);

function analyze(error, test1, test2) {
    if (error) {
        console.log(error);
    }
    console.log(d3.merge([test1, test2]));
    var data = d3.merge([test1, test2]);
    //readfile(test1);
    //readfile(test2);
    //console.log(test1);
    //console.log(test2);
}

function readfile(filename) {
    d3.csv("test2.csv", function (data) {
        data.forEach(function (d) {
            d.Hora = d["Hora"],
                d.Clave_del_nodo = +d["Clave del nodo"],
                d.Precio_marginal_local = +d["Precio marginal local ($/MWh)"],
                d.Componente_de_energia = +d["Componente de energia ($/MWh)"],
                d.Componente_de_perdidas = +d["Componente de perdidas ($/MWh)"],
                d.Componente_de_congestion = +d["Componente de congestion ($/MWh)"]
        });
        console.log(data);
    });
}

var width = 420,
    barHeight = 20;

var x = d3.scale.linear()
    .domain([0, d3.max(data)])
    .range([0, width]);

var chart = d3.select(".chart")
    .attr("width", width)
    .attr("height", barHeight * data.length);

var bar = chart.selectAll("g")
    .data(data)
    .enter().append("g")
    .attr("transform", function (d, i) {
        return "translate(0," + i * barHeight + ")";
    });

bar.append("rect")
    .attr("width", x)
    .attr("height", barHeight - 1);

bar.append("text")
    .attr("x", function (d) {
        return x(d) - 3;
    })
    .attr("y", barHeight / 2)
    .attr("dy", ".35em")
    .text(function (d) {
        return d;
    });