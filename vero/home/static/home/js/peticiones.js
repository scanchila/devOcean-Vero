const url = "http://localhost:8000/";

async function traerActividades() {
  //Almecena los datos en JSON
  let da = {
    "user": estado,
    "sentimientoInicial":sentInicial,
    "sentimientoFinal":sentFinal
  };
  try {
    $.ajax({
      url: url + "traerActividades/",
      type: "POST",
      data: da,
      cache: false,
      dataType: "json",
      success: function (resp) {
        console.log("resp: " + resp.respuesta);
        return resp.respuesta
      }
    });
  }
  catch (error) {
    console.log(error);
  }
}