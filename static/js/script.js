// ACTIVE NAV-LINK
$(document).ready(function() {
    $('li.active').removeClass('active');
    $('a[href="' + location.pathname + '"]').closest('li').addClass('active'); 
});

// FIXED HEADER ON SCROLL UP
$(document).ready(function() {
    var previousScroll = 0,
        headerOffset = $('#menu').offset().top;
    $('#menu-wrap').height($('#menu').height());
    $(window).scroll(function() {
        var currentScroll = $(this).scrollTop();
        if(currentScroll > headerOffset) {
            if (currentScroll > previousScroll) {
                $('#menu').fadeOut();
            } else {
                $('#menu').fadeIn();
                $('#menu').addClass('fixed');
            }
        } else {
             $('#menu').removeClass('fixed');   
        }
        previousScroll = currentScroll;
    });
});