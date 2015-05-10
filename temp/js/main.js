$loginBtn = $('#login-btn');
$taMainPage = $('#ta-main-page');
$loginBtn.on('click', function(event) {
    event.preventDefault();
    $('.wrapper').addClass('form-success');
    PageTransitions.nextPage($taMainPage);
    $loginBtn.addClass('loading');
    setTimeout(function() {
        // PageTransitions.nextPage($taMainPage);
        $loginBtn.removeClass('loading');
    }, 3000);
})
