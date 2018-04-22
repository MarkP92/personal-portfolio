// FIXED MENU AFTER SCROLL
$(window).scroll(function(){
    if ($(window).scrollTop() >= 700) {
       $('nav').addClass('nav-bg');
    }
    else {
       $('nav').removeClass('nav-bg');
    }
});

// ACTIVE NAV-LINK
$(document).ready(function() {
    $('li.active').removeClass('active');
    $('a[href="' + location.pathname + '"]').closest('li').addClass('active'); 
});


