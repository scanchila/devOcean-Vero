const url = "http://localhost:8000/";
document.getElementById('close-image1').onclick = function () {
  swal({
    title: "Gracias por la información!",
    text: "Cuenta con nosotros!",
    icon: "success",
    button: "ok",
  }).then(async function () {
    var ans = await responderEncuesta(2)
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
    var ans = await responderEncuesta(6)
    window.location.href = "/../";
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
    var ans = await responderEncuesta(4)
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
    var ans = await responderEncuesta(5)
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
    var ans = await responderEncuesta(7)
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
    var ans = await responderEncuesta(8)
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
    var ans = await responderEncuesta(1)
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
    var ans = await responderEncuesta("JUAN","energica","triste")
    window.location.href = "../";
  }).then(function () {
    window.location.href = "/../";
  })
  return false;
}

async function responderEncuesta(estado,sentInicial,sentFinal) {
  //Almecena los datos en JSON
  let da = {
    "user": estado,
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
        console.log("resp: " + resp.respuesta);
      }
    });
  }
  catch (error) {
    console.log(error);
  }

}
