const url = "http://localhost:8000/";
document.getElementById('close-image1').onclick = function () {
  swal({
    title: "Gracias por la información!",
    text: "Cuenta con nosotros!",
    icon: "success",
    button: "ok",
  }).then(async function () {
    console.log(readCookie("token"))
    var ans = await responderEncuesta(readCookie("token"),"enérgico");
    window.location.href = "/../";
  })
  return false;
}

document.getElementById('close-image2').onclick = function () {
  swal({
    title: "Gracias por la información!",
    text: "Cuenta con nosotros!",
    icon: "success",
    button: "ok",
  }).then(async function () {
    var ans = await responderEncuesta(readCookie("token"),"estresado");
    window.location.href = "/../";
  })
  return false;
}
document.getElementById('close-image3').onclick = function () {
  alert('boton')
  swal({
    title: "Gracias por la información!",
    text: "Cuenta con nosotros!",
    icon: "success",
    button: "ok",
  }).then(async function () {
    var ans = await responderEncuesta(readCookie("token"),"cansado");
    window.location.href = "/../";
  })
  return false;
}
document.getElementById('close-image4').onclick = function () {
  swal({
    title: "Gracias por la información!",
    text: "Cuenta con nosotros!",
    icon: "success",
    button: "ok",
  }).then(async function () {
    var ans = await responderEncuesta(readCookie("token"),"asustado");
    window.location.href = "/../";
  })
  return false;
}
document.getElementById('close-image5').onclick = function () {
  swal({
    title: "Gracias por la información!",
    text: "Cuenta con nosotros!",
    icon: "success",
    button: "ok",
  }).then(async function () {
    var ans = await responderEncuesta(readCookie("token"),"enojado");
    window.location.href = "/../";
  })
  return false;
}
document.getElementById('close-image6').onclick = function () {
  swal({
    title: "Gracias por la información!",
    text: "Cuenta con nosotros!",
    icon: "success",
    button: "ok",
  }).then(async function () {
    var ans = await responderEncuesta(readCookie("token"),"triste");
    window.location.href = "/../";
  })
  return false;
}
document.getElementById('close-image7').onclick = function () {
  swal({
    title: "Gracias por la información!",
    text: "Cuenta con nosotros!",
    icon: "success",
    button: "ok",
  }).then(async function () {
    var ans = await responderEncuesta(readCookie("token"),"feliz");
    window.location.href = "/../";
  })
  return false;
}
document.getElementById('close-image8').onclick = function () {
  swal({
    title: "Gracias por la información!",
    text: "Cuenta con nosotros!",
    icon: "success",
    button: "ok",
  }).then(async function () {
    var ans = await responderEncuesta(readCookie("token"),"amigable");
    window.location.href = "/../";
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
