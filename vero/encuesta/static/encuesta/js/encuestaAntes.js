const url = 'http://localhost:8000/'

const confirmFeeling = (feeling, activity_id, before) => {
    swal({
        title: 'Gracias por la información!',
        text: 'Cuenta con nosotros!',
        icon: 'success',
        button: 'ok',
    }).then(async function () {
        // console.log(
        //     `/personalActivities/personalActivity/${activity_id}/${feeling}`
        // )
        // console.log(feeling, activity_id, before)
        window.token = feeling
        setCookie(token)
        window.location.href = `/personalActivities/personalActivity/${activity_id}/${feeling}`
    })
    return false
}

async function responderEncuesta(estado, sentInicial, sentFinal) {
    //Almecena los datos en JSON
    let da = {
        user: estado,
        sentimientoInicial: sentInicial,
        sentimientoFinal: sentFinal,
    }
    try {
        $.ajax({
            url: url + 'encuesta/recibirEncuesta/',
            type: 'POST',
            data: da,
            cache: false,
            dataType: 'json',
            success: function (resp) {
                alert('resp: ' + resp.respuesta)
                return resp
            },
        })
    } catch (error) {
        console.log(error)
    }
}

function setCookie(token) {
    document.cookie =
        'token=' + encodeURIComponent(token) + '; max-age=3600; path=/'
}

function readCookie(name) {
    return (
        decodeURIComponent(
            document.cookie.replace(
                new RegExp(
                    '(?:(?:^|.*;)\\s*' +
                        name.replace(/[\-\.\+\*]/g, '\\$&') +
                        '\\s*\\=\\s*([^;]*).*$)|^.*$'
                ),
                '$1'
            )
        ) || null
    )
}

function deleteCookie() {
    document.cookie = 'token=; max-age=0; path=/'
}
