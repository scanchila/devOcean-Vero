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

var recurso = "";
document.getElementById('btnFiltroActividadesInd').onclick = async function(){
        var actividad = "";
        var tiempo = $('#sliderTime').val()
        if ($('.check-act').is(":checked")){
            actividad = "Respiración"
        }else if ($('.check-actT').is(":checked")){
            actividad = "Estiramientos"
        }
    window.location.href="actividad.html";
      var ans = await verActividadIndividual(actividad, recurso, tiempo);

}

function cambioRecurso(recursoSelec){
        recurso = recursoSelec;
}

//Consultar actividad individual
async function verActividadIndividual(actividad, recurso, tiempo){
    let data = {
        "actividad": actividad,
        "recurso": recurso,
        "tiempo": tiempo
    };

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

function traerActividadIndividual(actividades) {
    $("#actividadPropuesta").empty();
    console.log(actividades)
    for (const actividad of actividades) {
        mostrarActividadIndividual(actividad['codActividad'],actividad['titulo'],actividad['nombreActividad'], actividad['tipo'], actividad['url']);

    }
}



function mostrarActividadIndividual(codActividad, titulo, nombreActividad, tipo, url) {
    actividadC = "";
    if (tipo == "Video") {
        actividadC = '<h2 id="' + codActividad + '" class="titulos" >' + titulo + '</h2> <div class="contenedor-video"> <iframe  src="' + url + '" frameborder="0"  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>' +
                    '</div> ';
    } else if (tipo == "Audio") {
        actividadC = '<h2 id="' + codActividad + '" class="titulos" >' + titulo + '</h2> <div class="contenedor-audio"> <iframe  src="' + url + '" frameborder="0"  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>' +
                    '</div> ';
    }else if (tipo == "Texto"){
        actividadC = '<h2 id="' + codActividad + '" class="titulos" >' + titulo + '</h2> <div class="contenedor-texto"> <iframe  src="' + url + '" frameborder="0"  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>' +
                    '</div> '; //Agregar el visualizador de Lady
    }
    
    
    $("#actividadPropuesta").append(actividadC);

}