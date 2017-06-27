$(document).ready(function() {
    $('.top_menu').on('click', 'a.can_open', function(e) {
        e.preventDefault();
        $(this).parent().siblings().find('div').slideUp();
        $(this).next().slideToggle();
    });

    $('.about_company').click(function(e) {
        e.preventDefault();
        $('section.slider').hide();
        $('.unslider-nav').hide();
        $('section.about_block').show();
    });
    $('#about_company_back').click(function(e) {
        e.preventDefault();
        $('section.about_block').hide();
        $('section.slider').show();
        $('.unslider-nav').show();
    });

    
});
