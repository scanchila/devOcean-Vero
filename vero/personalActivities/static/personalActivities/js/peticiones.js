// Solicitar Actividad Individual
var respuesta = "";
async function enviarActividadIndividual(tipo, recurso, tiempo){
    //Almecena los datos en JSON
    let da = {
        "tipo": tipo,
        "recurso": recurso,
        "tiempo": tiempo,
        "csrfmiddlewaretoken": window.CSRF_TOKEN
    };
    console.log(da)
    try {
        $.ajax({
            url: url + "personalActivities/recibirActividad/",
            type: "POST",
            data: da,
            cache: false,
            dataType: "json",
            success: function (resp) {
                console.log("resp: " + resp.respuesta);
            }
        });
    }
    catch(error){
        console.log(error);
    }
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

