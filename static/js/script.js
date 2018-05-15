// ACTIVE NAV-LINK
$(document).ready(function() {
    $('li.active').removeClass('active');
    $('a[href="' + location.pathname + '"]').closest('li').addClass('active'); 
});

// FADE IN ANIMATION FOR ABOUT SECTION
// $(window).scroll(function () {
//     var topDivHeight = $(".hero-section").height();
//     var viewPortSize = $(window).height();
    
//     var triggerAt = 400;
//     var triggerHeight = (topDivHeight - viewPortSize) + triggerAt;

//     if ($(window).scrollTop() >= triggerHeight) {
//         $('#about-text').css('visibility', 'visible').hide().fadeIn();
//         $('.skills').css('visibility', 'visible').hide().fadeIn(2500);
//         $(this).off('scroll');
//     }
// });

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