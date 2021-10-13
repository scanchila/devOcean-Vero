const url = "http://localhost:8000/";
document.getElementById('close-image1').onclick = function () {
  swal({
    title: "Gracias por la información!",
    text: "Cuenta con nosotros!",
    icon: "success",
    button: "ok",
  }).then(async function () {
    window.token = "enérgico";
    setCookie(token);
    window.location.href = "/personalActivities/actividad";
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
    window.token = "estresado";
    setCookie(token);
    window.location.href = "/personalActivities/actividad";
  })
  return false;
}
document.getElementById('close-image3').onclick = function () {
  swal({
    title: "Gracias por la información!",
    text: "Cuenta con nosotros!",
    icon: "success",
    button: "ok",
  }).then(async function () {
    window.token = "cansado";
    setCookie(token);
    window.location.href = "/personalActivities/actividad";
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
    window.token = "asustado";
    setCookie(token);
    window.location.href = "/personalActivities/actividad";
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
    window.token = "enojado";
    setCookie(token);
    window.location.href = "/personalActivities/actividad";
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
    window.token = "triste";
    setCookie(token);
    window.location.href = "/personalActivities/actividad";
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
    window.token = "feliz";
    setCookie(token);
    window.location.href = "/personalActivities/actividad";
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
    window.token = "amigable";
    setCookie(token);
    window.location.href = "/personalActivities/actividad";
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
