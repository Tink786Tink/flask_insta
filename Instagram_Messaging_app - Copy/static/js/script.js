const showLoader = () => $("#loader").css("display", "flex");
const hideLoader = () => $("#loader").hide();

// hide cookie modal
const hideCookieModal = () => $("#cookie-modal").removeClass("show");

!(function ($) {
    "use strict";

    hideLoader();

    // accept cookie handler
    $("#cookie-modal .action .accept").click(function (e) {
        e.preventDefault();

        $.get(e.target.href);
        hideCookieModal();
    });

    // testimonial slider
    $("#testimonial-slider").slick({
        dots: true,
        infinite: true,
        autoplay: true,
        speed: 500,
        slidesToShow: 1,
        cssEase: "linear",
        arrows: false,
    });

    $(".togglePassword").click(function () {
        $(this).find(".bi").toggleClass("bi-eye-slash bi-eye");
        var pass = $(this).siblings("input");
        pass.attr("type") === "password"
            ? pass.attr("type", "text")
            : pass.attr("type", "password");
    });
})(jQuery);
