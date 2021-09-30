document.getElementById('BotonFinalizarSesion').onclick = function(){
    swal({
        title: "¡Gracias por participar en esta actividad!",
        text: "Te esperamos pronto en otra actividad",
        icon: "success",
        button: "ok",
      }).then(function () {
        window.location.href="/encuesta/";
    })
    return false;
      
}

//Consultar actividad individual
async function verActividadIndividual() {
    var USUARIO = JSON.parse(readCookie('token'));
    let data = {
        "idUsuario": USUARIO['id']
    }
    console.log(JSON.stringify(data));
    try {
        result = await $.ajax({
            url: url + "/verActividadIndividual",
            data: JSON.stringify(data),
            type: "POST",
            dataType: 'json',
            contentType: "application/json; charset=utf-8"
        })
        if (result.status == 200) {
            console.log(result.info)
            traerActividadIndividual(result.info)
        } else {
            console.log(result.status)
            swal("No se han encontrado coincidencias con tu búsqueda", {
                icon: "error"
            });

        }
    } catch (error) {
        console.log(error)
        return 0;
    }
    return true;
}

//Funcion para realizar la busqueda de las ofertas compradas
function traerActividadIndividual(actividades) {
    $("#actividadPropuesta").empty();
    console.log(actividades)
    for (const actividad of actividades) {
        mostrarActividadIndividual(actividad['codActividad'],actividad['titulo'],actividad['nombreActividad'], actividad['tipo'], actividad['url']);

    }
}



function mostrarActividadIndividual(codActividad, titulo, nombreActividad, tipo, url) {
    if (tipo == "Video") { 
        actividadC = "";
        actividadC = '<h2 id="' + codActividad + '" class="titulos" >' + titulo + '</h2> <div class="contenedor-video"> <iframe  src="' + url + '" frameborder="0"  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>' +
                    '</div> ';
    } else if (tipo == "Audio") {


    }else{

    }
    
    
    $("#actividadPropuesta").append(actividadC);

}