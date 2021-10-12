
document.getElementById('btnFiltroActividadesInd').onclick = async function(){

        var actividad = "";
        var tiempo = $('#sliderTime').val();
        let actividades = document.getElementsByName('check');
        actividades.forEach((check) => {
                if (check.checked=== true) {
                    actividad = check.value;
                }
            });
    //  var ans = await verActividadIndividual(actividad, recurso, tiempo);
    var ans = await enviarActividadIndividual(actividad, recurso, tiempo);
        window.location.href="/encuesta/encuestaAntes";

}