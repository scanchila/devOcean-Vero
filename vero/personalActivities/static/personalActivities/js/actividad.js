
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
    if (tipo == "Video") { 
        imagen="";
        actividadC = "";
        actividadC = '<h2 id="' + codActividad + '" class="titulos" >' + titulo + '</h2> <div class="contenedor-video"> <iframe  src="' + url + '" frameborder="0"  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>' +
                    '</div> ';
    } else if (tipo == "Audio") {
        imagen = "/./static/personalActivities/recursos/audios/img/Fondo.jpg";
        actividadC = ""; 
        actividadC = '<video controls="" autoplay="" name="media"><source src=" ' + url + ' " type="audio/mpeg"></video>';
    }else{
        actividadC = ""; 
        actividadC = '<div class="container-fluid mt-3"> <div class="container-fluid"> <div class="row"> <div class="col-lg-12"> <div class="card gradient-1"> <div class="card-body">' +
                      ' <div class="d-inline-block">   <h3 class="text-white">' + titulo + '</h3>   </div>  </div>  </div>  </div>  </div> </div>  <div class="container-fluid">' +
                        '<div class="row"> <div class="col-lg-12">  <div class="card">  <iframe src="' + url + '"> </iframe> </div> </div> </div> </div>  </div>';
    }
    
    
    $("#actividadPropuesta").append(actividadC);
    const newMusicPlayer = new musicPlayer();
}