const endSession = (activity_id) => {
    swal({
        title: '¡Gracias por participar en esta actividad!',
        text: 'Te esperamos pronto en otra actividad',
        icon: 'success',
        button: 'ok',
    }).then(function () {
        // console.log(
        //     `/personalActivities/personalActivity_finish/${activity_id}/`
        // )
        window.location.href = `/personalActivities/personalActivity_finish/${activity_id}/`
    })
    return false
}
