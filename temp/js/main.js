$iterate = $('#iterateEffects');
$iterate.on('click', function() {
    PageTransitions.nextPage();
})

$loginBtn = $('#loginBtn');
$loginPage = $('#loginPage');
$loginBtn.on('click', function(event) {
    event.preventDefault();
    $('.wrapper').addClass('form-success');

    $loginBtn.addClass('loading');
    setTimeout(function() {
        //PageTransitions.nextPage($loginPage);
        $loginBtn.removeClass('loading');
    }, 3000);
})
