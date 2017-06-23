//
//   var   Username =  document.getElementById('username').value
//
//
// var gg = $('#run').value;
// var gg1 = $('#username').val();
//
// console.log(gg1);
// if (gg1.length >= 0  ){
//   $.ajax({
//             type: "POST",
//             url: "http://0.0.0.0:8261/follow",
//             dataType: "json",
//             data: {
//                 o:gg1
//             }
//
//         });
// }
// else{
//
// }
// if (gg1.length >= 0  ){
//   $.ajax({
//             type: "POST",
//             url: "http://0.0.0.0:8261/AutoRound",
//             dataType: "json",
//             data: {
//                 o:gg1
//             }
//
//         });
// }
// else{
// //
// // }
// $(document).ready(function() {
//   $("#popup").modal({
//       show: false,
//       backdrop: 'static'
//   });
//
//   $("#click-me").click(function() {
//      $("#popup").modal("show");
//   });
// });

// $(document).ready(function () {
//
//    // Attach Button click event listener
//   $("#myBtn").click(function(){
//
//        // show Modal
//        $('#myModal').modal({
//   backdrop: 'static',
//   keyboard: true,
//   show: true //prevent closing with Esc button (if you want this too)
// })
//   });
// });

$(document).ready(function () {
var navListItems = $('div.setup-panel div a'),
        allWells = $('.setup-content'),
        allNextBtn = $('.nextBtn');

allWells.hide();

navListItems.click(function (e) {
    e.preventDefault();
    var $target = $($(this).attr('href')),
            $item = $(this);

    if (!$item.hasClass('disabled')) {
        navListItems.removeClass('btn-primary').addClass('btn-default');
        $item.addClass('btn-primary');
        allWells.hide();
        $target.show();
        $target.find('input:eq(0)').focus();
    }
});

allNextBtn.click(function(){
    var curStep = $(this).closest(".setup-content"),
        curStepBtn = curStep.attr("id"),
        nextStepWizard = $('div.setup-panel div a[href="#' + curStepBtn + '"]').parent().next().children("a"),
        curInputs = curStep.find("input[type='text'],input[type='url']"),
        isValid = true;

    $(".form-group").removeClass("has-error");
    for(var i=0; i<curInputs.length; i++){
        if (!curInputs[i].validity.valid){
            isValid = false;
            $(curInputs[i]).closest(".form-group").addClass("has-error");
        }
    }

    if (isValid)
        nextStepWizard.removeAttr('disabled').trigger('click');
});

$('div.setup-panel div a.btn-primary').trigger('click');
});
