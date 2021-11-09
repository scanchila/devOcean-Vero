const url = "http://localhost:8000/";
let recurso = "";
function setCookie(token) {
    document.cookie = "token=" + encodeURIComponent(token) + "; max-age=3600; path=/";
}

function readCookie(name) {
    return decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*" + name.replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=\\s*([^;]*).*$)|^.*$"), "$1")) || null;
}

function deleteCookie() {
    document.cookie = "token=; max-age=0; path=/";
}

function cambioRecurso(recursoSelec){
    recurso = recursoSelec;
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
    actividadC = '<h2 " class="titulos" >' + titulo +' </h2><center> <video controls="" autoplay="" name="media" ><source src=" ' + url + ' " type="audio/mpeg"></video></center> <br><br><br>';
}else{
    actividadC = ""; 
    actividadC = '<div class="container-fluid mt-3"> <div class="container-fluid"> <div class="row"> <div class="col-lg-12"> <div class="card gradient-1"> <div class="card-body">' +
                  ' <div class="d-inline-block">   <h3 class="text-white">' + titulo + '</h3>   </div>  </div>  </div>  </div>  </div> </div>  <div class="container-fluid">' +
                    '<div class="row"> <div class="col-lg-12">  <div class="card">  <iframe src="' + url + '"> </iframe> </div> </div> </div> </div>  </div>';
}

$("#actividadPropuesta").empty();
$("#actividadPropuesta").append(actividadC);
const newMusicPlayer = new musicPlayer();
}
