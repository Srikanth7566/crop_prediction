function onPageLoad(){
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_state_names";
    $.get(url, function(data, status){
        console.log("got response for get states request");
        if(data){
            var state = data.state
            var uistate = document.getElementById("uistate");
            $('#uistate').empty();
            for (var i in state){
                var opt = new Option(state[i]);
                $('#uistate').append(opt);
            }
        }
    });
}


function onClickedPredictCrop(){
    console.log("predict crop button pressed");
    var state = document.getElementById("uistate");
    var season = document.getElementById('uiseason');
    var soil = document.getElementById('uisoil');
    var rainfall = document.getElementById('uirainfall');
    var precrop = document.getElementById('uiPredictCrop');

    var url = "http://127.0.0.1:5000/predict_crop";

    $.post(url, {
        state: state.value,
        season: season.value,
        soil: soil.value,
        rainfall: parseInt(rainfall.value)
    }, function(data, status){
        console.log(data.predicted_crop);
        precrop.innerHTML = "<h2>" + data.predicted_crop.toString() + "</h2>";
        console.log(status);
    })
}


window.onload = onPageLoad;
