
document.getElementById('btnFiltroActividadesInd').onclick = async function(){

        var actividad = "";
        var tiempo = $('#sliderTime').val()
        if ($('.check-act').is(":checked")){
            actividad = "Respiración"
        }else if ($('.check-actT').is(":checked")){
            actividad = "Estiramientos"
        }
    window.location.href="/encuesta/encuestaAntes";
      var ans = await verActividadIndividual(actividad, recurso, tiempo);

}