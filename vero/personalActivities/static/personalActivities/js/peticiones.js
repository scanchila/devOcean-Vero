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