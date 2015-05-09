$iterate = $( '#iterateEffects' );
$iterate.on('click', function() {
	PageTransitions.nextPage();
})

$login = $('#login');
$loginPage = $('#loginPage');
$login.on('click', function() {
	PageTransitions.nextPage($loginPage);
})