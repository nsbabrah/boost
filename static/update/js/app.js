$(document).ready(function() {
    $(".plus-btn").click(function() {
        if ($(this).find(".fa-plus").is(':visible')) {
            $("html, body").animate({ scrollTop: $(this).offset().top }, 1000);
        }
        $(this).children().toggle();
    });
    function myFunc(vars) {
    return vars
}
    $(window).on('scroll', function() {
        var value = $(this).scrollTop();
        if (value > 170) {
            $("#trynow").addClass("try_now_in");
            $("#trynow").removeClass("try_now");
        } else {
            $("#trynow").removeClass("try_now_in");
            $("#trynow").addClass("try_now");
        }
    });
    // $("#cont").slider()
    $("#cont").slider({
        autoMove: false,
        autoMoveOptions: {
            interval: 5000,
            pauseOnHover: true,
        },
        buttonsEnabled: true,
        buttonsOptions: {
            leftText: "<",
            rightText: ">",
        },
        bulletsEnabled: true,
        slideWithFinger: true,
        slideWithCursor: true,
    })
});