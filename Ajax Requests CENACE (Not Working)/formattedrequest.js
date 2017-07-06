var cargaDatos = function () {
  $.ajax({
      type: "post",
      url: "http://www.cenace.gob.mx/ajax.aspx",
      data: "{}",
      beforeSend: function(jqXHR, settings) {
        console.log(settings.url);
      },
      success: function (response) {
       ajaxSuccess(response);
       console.log(response);
       console.log (this.url);
      }
  });
}
 if (!datosHistoricoIncluidos) {
     cargaDatos();
  }
setInterval(function () {
    cargaDatos();
}, 3000);

function ajaxSuccess(response) {
    if (response == undefined || response == null || response == '<0/>' || response == '') {
        return;
    }
    var respuesta = trim(response);
    var valores = respuesta.split("&");
    // BC
    var ContentPlaceHolder1_demandaBC = valores[0] == undefined ? '': valores[0];
      console.log("demandaBC: " + ContentPlaceHolder1_demandaBC)
    var ContentPlaceHolder1_generacionBC = valores[1] == undefined ? '' : valores[1];
      console.log("generacionBD: " + ContentPlaceHolder1_generacionBC)
    var ContentPlaceHolder1_enlaceBC = valores[24] == undefined ? '' : valores[24];
      console.log("enlaceBC: " + ContentPlaceHolder1_enlaceBC)

    // BSC
    var ContentPlaceHolder1_demandaBCS = valores[2] == undefined ? '' : valores[2];
      console.log("demandaBCS: " + ContentPlaceHolder1_demandaBCS)
    var ContentPlaceHolder1_generacionBCS = valores[3] == undefined ? '' : valores[3];
      console.log("generacionBCS: " + ContentPlaceHolder1_generacionBCS)
    var ContentPlaceHolder1_enlaceBCS = valores[25] == undefined ? '' : valores[25];
      console.log("enlaceBCS: " + ContentPlaceHolder1_enlaceBCS)

    // CEN
    var ContentPlaceHolder1_demandaCEN = valores[4] == undefined ? '' : valores[4];
      console.log("demandaCEN: " + ContentPlaceHolder1_demandaCEN)
    var ContentPlaceHolder1_generacionCEN = valores[5] == undefined ? '' : valores[5];
      console.log("generacionCEN: " + ContentPlaceHolder1_generacionCEN)
    var ContentPlaceHolder1_enlaceCEN = valores[26] == undefined ? '' : valores[26];
      console.log("enlaceCEN: " + ContentPlaceHolder1_enlaceCEN)

    // NE
    var ContentPlaceHolder1_demandaNE = valores[6] == undefined ? '' : valores[6];
      console.log("demandaNE: " + ContentPlaceHolder1_demandaNE)
    var ContentPlaceHolder1_generacionNE = valores[7] == undefined ? '' : valores[7];
      console.log("generacionNE: " + ContentPlaceHolder1_generacionNE)
    var ContentPlaceHolder1_enlaceNE = valores[27] == undefined ? '' : valores[27];
      console.log("enlaceNE: " + ContentPlaceHolder1_enlaceNE)

    // NO
    var ContentPlaceHolder1_demandaNO = valores[8] == undefined ? '' : valores[8];
      console.log("demandaNO: " + ContentPlaceHolder1_demandaNO)
    var ContentPlaceHolder1_generacionNO = valores[9] == undefined ? '' : valores[9];
      console.log("generacionNO: " + ContentPlaceHolder1_generacionNO)
    var ContentPlaceHolder1_enlaceNO = valores[28] == undefined ? '' : valores[28];
      console.log("enlaceNO: " + ContentPlaceHolder1_enlaceNO)

    // NTE
    var ContentPlaceHolder1_demandaNTE = valores[10] == undefined ? '' : valores[10];
      console.log("demandaNTE: " + ContentPlaceHolder1_demandaNTE)
    var ContentPlaceHolder1_generacionNTE = valores[11] == undefined ? '' : valores[11];
      console.log("generacionNTE: " + ContentPlaceHolder1_generacionNTE)
    var ContentPlaceHolder1_enlaceNTE = valores[29] == undefined ? '' : valores[29];
      console.log("enlaceNTE: " + ContentPlaceHolder1_enlaceNTE)

    var ContentPlaceHolder1_demandaOCC = valores[12] == undefined ? '' : valores[12];
      console.log("demandaOCC: " + ContentPlaceHolder1_demandaOCC)
    var ContentPlaceHolder1_generacionOCC = valores[13] == undefined ? '' : valores[13];
      console.log("generacionOCC: " + ContentPlaceHolder1_generacionOCC)
    var ContentPlaceHolder1_enlaceOCC = valores[30] == undefined ? '' : valores[30];
      console.log("enlaceOCC: " + ContentPlaceHolder1_enlaceOCC)

    var ContentPlaceHolder1_demandaOR = valores[14] == undefined ? '' : valores[14];
      console.log("demandaOR: " + ContentPlaceHolder1_demandaOR)
    var ContentPlaceHolder1_generacionOR = valores[15] == undefined ? '' : valores[15];
      console.log("generacionOR: " + ContentPlaceHolder1_generacionOR)
    var ContentPlaceHolder1_enlaceOR = valores[31] == undefined ? '' : valores[31];
      console.log("enlaceOR: " + ContentPlaceHolder1_enlaceOR)

    var ContentPlaceHolder1_demandaPEN = valores[16] == undefined ? '' : valores[16];
      console.log("demandaPEN: " + ContentPlaceHolder1_demandaPEN)
    var ContentPlaceHolder1_generacionPEN = valores[17] == undefined ? '' : valores[17];
      console.log("generacionPEN: " + ContentPlaceHolder1_generacionPEN)
    var ContentPlaceHolder1_enlacePEN = valores[32] == undefined ? '' : valores[32];
      console.log("enlacePEN: " + ContentPlaceHolder1_enlacePEN)

    var ContentPlaceHolder1_demandaNACNeta = valores[19] == undefined ? '' : valores[19];
      console.log("demandaNACNeta: " + ContentPlaceHolder1_demandaNACNeta)
    var ContentPlaceHolder1_generacionNAC = valores[20] == undefined ? '' : valores[20];
      console.log("generacionNAC: " + ContentPlaceHolder1_generacionNAC)
    var ContentPlaceHolder1_enlaceNAC = valores[23] == undefined ? '' : valores[23];
      console.log("enlaceNAC: " + ContentPlaceHolder1_enlaceNAC)

    var ContentPlaceHolder1_datetimeBC = valores[21] == undefined ? '' : valores[21];
    var ContentPlaceHolder1_datetimeBCS = valores[21] == undefined ? '' : valores[21];
    var ContentPlaceHolder1_datetimeCEN = valores[21] == undefined ? '' : valores[21];
    var ContentPlaceHolder1_datetimeNE = valores[21] == undefined ? '' : valores[21];
    var ContentPlaceHolder1_datetimeNO = valores[21] == undefined ? '' : valores[21];
    var ContentPlaceHolder1_datetimeNTE = valores[21] == undefined ? '' : valores[21];
    var ContentPlaceHolder1_datetimeOCC = valores[21] == undefined ? '' : valores[21];
    var ContentPlaceHolder1_datetimeOR = valores[21] == undefined ? '' : valores[21];
    var ContentPlaceHolder1_datetimePEN = valores[21] == undefined ? '' : valores[21];
      console.log("datetime: " + ContentPlaceHolder1_datetimeBC)


    //var ContentPlaceHolder1_datetimeNAC = valores[22] == undefined ? '' : valores[22];
    var ContentPlaceHolder1_datetimeNAC = valores[21] == undefined ? '' : valores[21];
      console.log("datetimeNAC: " + ContentPlaceHolder1_datetimeNAC)
    var ContentPlaceHolder1_datetimeNAC2 = valores[21] == undefined ? '' : valores[21];
      console.log("datetimeNAC2: " + ContentPlaceHolder1_datetimeNAC2)

    var ContentPlaceHolder1_demandaNAC2 = valores[19] == undefined ? '' : valores[19];
      console.log("demandaNAC2: " + ContentPlaceHolder1_demandaNAC2)
    var ContentPlaceHolder1_pronosticoNACNeto = valores[23] == undefined ? '' : valores[23];
      console.log("pronosticoNACNeto: " + ContentPlaceHolder1_pronosticoNACNeto)
    var ContentPlaceHolder1_datetimeNAC_en = valores[33] == undefined ? '' : valores[33];
      console.log("datetimeNAC_en: " + ContentPlaceHolder1_datetimeNAC_en)
}

function trim(s) {
    while ((s.substring(0, 1) === ' ') || (s.substring(0, 1) === '\n') || (s.substring(0, 1) === '\r')) {
        s = s.substring(1, s.length);
    }
    while ((s.substring(s.length - 1, s.length) === ' ') || (s.substring(s.length - 1, s.length) === '\n') || (s.substring(s.length - 1, s.length) === '\r')) {
        s = s.substring(0, s.length - 1);
    }
    return s;
};
