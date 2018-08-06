// ACTIVE NAV-LINK
$(document).ready(function() {
    $('li.active').removeClass('active');
    $('a[href="' + location.pathname + '"]').closest('li').addClass('active'); 
});

// FIXED HEADER ON SCROLL UP
$(document).ready(function() {
    var prevScroll = window.pageYOffset;
    $(window).scroll(function(){
        var currentScroll = window.pageYOffset;
            if (prevScroll > currentScroll) {
                $('header').addClass('sticky-top');
            } else {
                $('header').removeClass('sticky-top');
            }
            prevScroll = currentScroll;
    })
});