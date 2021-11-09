document.getElementById('closeEnterActivity').onclick = function () {
  swal({
    title: "Gracias por la información!",
    text: "Cuenta con nosotros!",
    icon: "success",
    button: "ok",
  }).then(async function () {
    //console.log(readCookie("token"))
    //var ans = await responderEncuesta(readCookie("token"),"enérgico");
    //window.location.href = "/../";
  })
  return false;
}

async function responderEncuesta(sentInicial,sentFinal) {
  //Almecena los datos en JSON
  let da = {
    "sentimientoInicial":sentInicial,
    "sentimientoFinal":sentFinal
  };
  try {
    $.ajax({
      url: url + "encuesta/recibirEncuesta/",
      type: "POST",
      data: da,
      cache: false,
      dataType: "json",
      success: function (resp) {
        alert("resp: " + resp.respuesta);
        return resp
      }
    });
  }
  catch (error) {
    console.log(error);
  }

}

function setCookie(token) {
  document.cookie = "token=" + encodeURIComponent(token) + "; max-age=3600; path=/";
}

function readCookie(name) {
  return decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*" + name.replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=\\s*([^;]*).*$)|^.*$"), "$1")) || null;
}

function deleteCookie() {
  document.cookie = "token=; max-age=0; path=/";
}
