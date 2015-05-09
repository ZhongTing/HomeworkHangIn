$iterate = $('#iterateEffects');
$iterate.on('click', function() {
    PageTransitions.nextPage();
})

$login = $('#loginBtn');
$loginPage = $('#loginPage');
$login.on('click', function(event) {
    event.preventDefault();
    $('.wrapper').addClass('form-success');
    PageTransitions.nextPage($loginPage);
})
