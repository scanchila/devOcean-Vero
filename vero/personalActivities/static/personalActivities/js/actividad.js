document.getElementById('BotonFinalizarSesion').onclick = function(){
    swal({
        title: "¡Gracias por participar en esta actividad!",
        text: "Te esperamos pronto en otra actividad",
        icon: "success",
        button: "ok",
      }).then(function () {
        window.location.href="/../encuesta/encuesta";
    })
    return false;
      
}
