var recurso = "";
document.getElementById('btnFiltroActividadesInd').onclick = async function(){
        var actividad = "";
        var tiempo = $('#sliderTime').val()
        if ($('.check-act').is(":checked")){
            actividad = "Respiración"
        }else if ($('.check-actT').is(":checked")){
            actividad = "Estiramientos"
        }

      var ans = await solicitarActividadIndividual(actividad, recurso, tiempo);
      window.location.href="/../";
}

function cambioRecurso(recursoSelec){
        recurso = recursoSelec;
}

async function solicitarActividadIndividual(actividad, recurso, tiempo){
    let data = {
        "actividad": actividad,
        "recurso": recurso,
        "tiempo": tiempo
    };

    try {
        result = await $.ajax({
            url: url + "/../../",
            data: JSON.stringify(data),
            type: "POST",
            dataType: 'json',
            contentType: "application/json; charset=utf-8"
        })
        console.log(result.responseJSON)
        return result.info;
    } catch (error) {
        console.log(error.responseJSON)
    }
}
