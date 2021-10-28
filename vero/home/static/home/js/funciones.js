
async function pedirActividades(){
    var activities = await traerActividades();
    for(let i=0; i < activities; i++){
        mostrarActividad(activities[i].pk, activities[i].fields.name, activities[i].fields.description, activities[i].fields.imageURL, activities[i].fields.duration);
    }
}

function mostrarActividad(id, nombre, descripcion, imagen, duracion){
    actividad = "";


    //$("#actividades").append(ofertasC);
}