var systemSetting = {
    offlineDemo: false,
    quicklogin: true
};

function isOfflineDemo() {
    return systemSetting.offlineDemo;
}

function init() {
    $taMainPage = $('#ta-main-page');
    $studentMainPage = $('#student-main-page');
    $correctHwPage = $("#correct-homework-page");
    $uploadHwPage = $("#upload-homework-page");

    if (isOfflineDemo) {
        initMockData();
    }
    initLoginPage();

    // API.user.login("t103598011@ntut.edu.tw", "test", function (success, data) {
    //     if (success) {
    //         //alert("hello ~ " + data["account"]);
    //         API.homework.list();
    //         API.homework.download(1);
    //     } else {
    //         alert("account or password error!!");
    //     }
    // });
}

function initMockData() {
    mockTa = {
        role: "ta"
    };
    mockStudent = {
        role: "Student"
    };
    var mockHwList = [{
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
    initHomeworkMenu(mockHwList);
}

function initLoginPage() {
    var doLogin = function () {
        var account = $("#account").val();
        var password = $("#password").val();
        if (isOfflineDemo()) {
            if (account === "ta") {
                currentUser.init(mockTa);
            } else {
                currentUser.init(mockStudent);
            }
            if (systemSetting.quicklogin) {
                turnToMainPage();
            } else {
                $loginBtn.addClass('loading');
                setTimeout(function () {
                    $loginBtn.removeClass('loading');
                    turnToMainPage();
                }, 2000);
            }
        } else {
            $loginBtn.addClass('loading');
            API.user.login(account, password, function (success, data) {
                // API.user.login("sdtlab@gmail.com", "test", function (success, data) {
                $loginBtn.removeClass('loading');
                if (success) {
                    currentUser.init(data);
                    API.homework.list(function (success, data) {
                        if (success) {
                            initHomeworkMenu(data.list)
                        }
                    });
                    turnToMainPage(data.name);
                } else {
                    alert("account or password error!!");
                }
            });
        }
    }
    $("#account").keyup(function (event) {
        if (event.keyCode == 13) {
            doLogin();
        }
    });
    $("#password").keyup(function (event) {
        if (event.keyCode == 13) {
            doLogin();
        }
    });
    $loginBtn = $('#login-btn');
    $loginBtn.on('click', function (event) {
        event.preventDefault();
        doLogin();
    })
}

function turnToMainPage(name) {
    if (currentUser.isTa()) {
        turnToTAPage(name);
    } else {
        turnToStudentPage(name);
    }
}

function turnToStudentPage(name) {
    PageTransitions.nextPage($studentMainPage);
    initToStudentPage(name);
}

function initToStudentPage(name) {
    $("#welcome-student-message").text("Welcome back, " + name);
}

function turnToTAPage(name) {
    PageTransitions.nextPage($taMainPage);
    initTAMainPage(name);
}

function turnToCorrectHomeworkPage(hwid, hwname) {
    PageTransitions.nextPage($correctHwPage);
    initCorrectHwPage(hwid, hwname);
}

function turnToUploadHomeworkPage(hwid, hwname) {
    PageTransitions.nextPage($uploadHwPage);
    initUploadHwPage(hwid, hwname);
};

function initTAMainPage(name) {
    $("#welcome-ta-message").text("Welcome back, " + name);
    initAssignPage();
}

function initHomeworkMenu(homeworkList) {
    var html = '';
    var count = 4;
    if (homeworkList.length != 0) {
        for (var i = homeworkList.length - 1; i >= 0; i--) {
            var hw = homeworkList[i];
            html = '<li data-hwid=' + hw.id + ' data-hwname=' + hw.name + '><a href="#">' + hw.name + '</a></li>' + html;
            if (i % count == 0 && i != 0) {
                html = '<li><a href="#">next</a><ul class="dl-submenu">' + html + '</ul></li>';
            }
        }
    } else {
        html = '<li><a href="#">homework list empty</a></li>';
    }
    $(".homework-menu ul.dl-menu").html(html);
    $('.homework-menu').removeData('dlmenu');
    $('.homework-menu').dlmenu({
        animationClasses: { in : 'dl-animate-in-4', out: 'dl-animate-out-4'
        }
    });
    $(".homework-menu li[data-hwid]").off().on('click', function () {
        if (currentUser.isTa()) {
            turnToCorrectHomeworkPage(this.dataset['hwid'], this.dataset['hwname']);
        } else {
            turnToUploadHomeworkPage(this.dataset['hwid'], this.dataset['hwname']);
        }
    })
}

function initAssignPage() {
    $("#assign-btn").off().on('click', function () {
        var year = $("#assign-hw-year").val();
        var name = $("#assign-hw-name").val();
        var score = $("#assign-hw-score").val();
        API.homework.create(year, name, score, function (success, data) {
            alert('success');
            PageTransitions.back();
            API.homework.list(function (success, data) {
                if (success) {
                    initHomeworkMenu(data.list)
                }
            });
        });
    });
}

function initCorrectHwPage(hwid, hwname) {
    $("#correct-hw-name").text(hwname);
    $("#download-hw").on('click', function () {
        API.homework.download(hwid, function () {
            alert("something wrong!");
        });
    });
}

function initUploadHwPage(hwid, hwname) {
    $("#upload-hw-name").text(hwname);
    $("#upload-hw").off().on('click', function () {
        var file = $("#homework-file-input")[0].files[0];
        API.homework.upload(hwid, file, function (success, data) {
            alert('success');
            PageTransitions.back();
        })
    })
}

$('.back').each(function () {
    $(this).on('click', function () {
        PageTransitions.back();
    })
});

$("*[data-nextpage]").each(function () {
    $(this).on('click', function () {
        $nextPage = $("#" + $(this).data('nextpage'));
        PageTransitions.nextPage($nextPage);
    });
});

init();
