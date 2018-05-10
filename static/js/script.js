

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
    
    var triggerAt = 400;
    var triggerHeight = (topDivHeight - viewPortSize) + triggerAt;

    if ($(window).scrollTop() >= triggerHeight) {
        $('#about-text').css('visibility', 'visible').hide().fadeIn();
        $('.skills').css('visibility', 'visible').hide().fadeIn(2500);
        $(this).off('scroll');
    }
});


// MENU BG AFTER SCROLL
// $(window).scroll(function(){
//     if ($(window).scrollTop() >= 700) {
//        $('#menu').addClass('nav-scroll-bg');
//     }
//     else {
//        $('#menu').removeClass('nav-scroll-bg');
//     }
// });

