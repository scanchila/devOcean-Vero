document.getElementById('close-image1').onclick = function(){
    swal({
      title: "Good job!",
      text: "You clicked the button!",
      icon: "success",
      button: "ok",
      }).then(function () {
        var ans = await responderEncuesta(2)
        window.location.href="/../";
    })
    return false;
}

document.getElementById('close-image2').onclick = function(){
  swal({
      title: "Good job!",
      text: "You clicked the button!",
      icon: "success",
      button: "ok",
    }).then(function () {
      var ans = await responderEncuesta(6)
      window.location.href="/../";
  })
  return false;
}
document.getElementById('close-image3').onclick = function(){
  swal({
      title: "Good job!",
      text: "You clicked the button!",
      icon: "success",
      button: "ok",
    }).then(function () {
      var ans = await responderEncuesta(4)
      window.location.href="/../";
  })
  return false;
}
document.getElementById('close-image4').onclick = function(){
  swal({
      title: "Good job!",
      text: "You clicked the button!",
      icon: "success",
      button: "ok",
    }).then(function () {
      var ans = await responderEncuesta(5)
      window.location.href="/../";
  })
  return false;
}
document.getElementById('close-image5').onclick = function(){
  swal({
      title: "Good job!",
      text: "You clicked the button!",
      icon: "success",
      button: "ok",
    }).then(function () {
      var ans = await responderEncuesta(7)
      window.location.href="/../";
  })
  return false;
}
document.getElementById('close-image6').onclick = function(){
  swal({
      title: "Good job!",
      text: "You clicked the button!",
      icon: "success",
      button: "ok",
    }).then(function () {
      var ans = await responderEncuesta(8)
      window.location.href="/../";
  })
  return false;
}
document.getElementById('close-image7').onclick = function(){
  swal({
      title: "Good job!",
      text: "You clicked the button!",
      icon: "success",
      button: "ok",
    }).then(function () {
      var ans = await responderEncuesta(1)
      window.location.href="/../";
  })
  return false;
}
document.getElementById('close-image8').onclick = function(){
  swal({
      title: "Good job!",
      text: "You clicked the button!",
      icon: "success",
      button: "ok",
    }).then(function () {
      var ans = await responderEncuesta(3)
      window.location.href="../";
  })
  return false;
}

async function responderEncuesta(estado) {
    //Almecena los datos en JSON
    let data = {
        "estado": estado
    };

    try {
        result = await $.ajax({
            url: url + "/feelings",
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