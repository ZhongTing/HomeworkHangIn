function init() {
    $taMainPage = $('#ta-main-page');
    initLoginPage();
}

function initLoginPage() {
    $loginBtn = $('#login-btn');
    $loginBtn.on('click', function(event) {
        event.preventDefault();
        turnInTAPage();
        $loginBtn.addClass('loading');
        setTimeout(function() {
            // turnInTAPage();
            $loginBtn.removeClass('loading');
        }, 3000);
    })
}

function turnInTAPage() {
    PageTransitions.nextPage($taMainPage);
    homeworkList = [{
        id: 1,
        name: 'homework1'
    }, {
        id: 2,
        name: 'homework2'
    }, {
        id: 3,
        name: 'homework3'
    }, {
        id: 4,
        name: 'homework4'
    }, {
        id: 5,
        name: 'homework5'
    }, {
        id: 6,
        name: 'homework6'
    }, {
        id: 7,
        name: 'homework7'
    }];
    // homeworkList = [];
    initTAMainPage(homeworkList);
}

function turnToCorrectHomeworkPage(hwid) {
    PageTransitions.nextPage($("#correct-homework-page"));
    initCorrectHwPage(hwid);
}

function initTAMainPage(homeworkList) {
    initHomeworkMenu(homeworkList);
}

function initHomeworkMenu(homeworkList) {
    var html = '';
    var count = 4;
    if (homeworkList.length != 0) {
        for (var i = homeworkList.length - 1; i >= 0; i--) {
            var hw = homeworkList[i];
            html = '<li data-hwid=' + hw.name + '><a href="#">' + hw.name + '</a></li>' + html;
            if (i % count == 0 && i != 0) {
                html = '<li><a href="#">next</a><ul class="dl-submenu">' + html + '</ul></li>';
            }
        }
    } else {
        html = '<li><a href="#">homework list empty</a></li>';
    }
    $("#homework-menu ul.dl-menu").html(html);
    $('#homework-menu').removeData('dlmenu');
    $('#homework-menu').dlmenu({
        animationClasses: { in : 'dl-animate-in-4', out: 'dl-animate-out-4'
        }
    });
    $("#homework-menu li[data-hwid]").on('click', function() {
        turnToCorrectHomeworkPage(this.dataset['hwid']);
    })
}

function initCorrectHwPage(hwid) {
    $("#correct-hw-name").text(hwid);
}

$('.back').each(function() {
    $(this).on('click', function() {
        PageTransitions.back();
    })
})

$("*[data-nextpage]").each(function() {
    $(this).on('click', function() {
        $nextPage = $("#" + $(this).data('nextpage'))
        PageTransitions.nextPage($nextPage);
    });
})

init();
