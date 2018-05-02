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

// FADE IN ANIMATION FOR ABOUT SECTION
$(window).scroll(function () {
    console.log($(window).scrollTop());
    var topDivHeight = $(".hero-section").height();
    var viewPortSize = $(window).height();
    
    var triggerAt = 300;
    var triggerHeight = (topDivHeight - viewPortSize) + triggerAt;

    if ($(window).scrollTop() >= triggerHeight) {
        $('#about-section').css('visibility', 'visible').hide().fadeIn();
        $('.skills').css('visibility', 'visible').hide().fadeIn(2500);
        $(this).off('scroll');
    }
});


