
  var   Username =  document.getElementById('username').value


var gg = $('#run').value;
var gg1 = $('#username').val();

console.log(gg1);
if (gg1.length >= 0  ){
  $.ajax({
            type: "POST",
            url: "http://0.0.0.0:8261/follow",
            dataType: "json",
            data: {
                o:gg1
            }

        });
}
else{

}
if (gg1.length >= 0  ){
  $.ajax({
            type: "POST",
            url: "http://0.0.0.0:8261/AutoRound",
            dataType: "json",
            data: {
                o:gg1
            }

        });
}
else{

}
