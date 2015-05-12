var api = (function () {
    var serverURL = "http://140.124.181.195:9000/";
    var accessToken = "";

    function request(type, action, data, needAccessToken, callback) {
        $.ajax({
            type: type,
            url: serverURL + action,
            beforeSend: function (request) {
                if (needAccessToken)
                    request.setRequestHeader("Authorization", accessToken);
            },
            data: data,
            success: function (data) {
                console.log(action, "=>", data);
                if (callback)
                    callback(true, data);
            },
            error: function (data) {
                if (callback)
                    callback(false, data.responseText);
            }
        });
    }

    function userlogin(account, password, callback) {
        var data = {
            account: account,
            password: password
        };
        request("POST", "api/user/login", data, false, function (success, data) {
            if (success) {
                accessToken = data.accessToken;
                console.log("AccessToken:", accessToken);
            }
            callback(success, data);
        });
    }

    function createHomework(year, name, totalScore, callback) {
        var data = {
            year: year,
            name: name,
            totalScore: totalScore,
        };
        request("POST", "api/homework/create", data, true, callback);
    }

    function listHomework(callback) {
        var data = {};
        request("GET", "api/homework/list", data, true, callback);
    }

    function uploadHomework(callback) {
        // http://stackoverflow.com/questions/5392344/sending-multipart-formdata-with-jquery-ajax
        var data;
        request("POST", "api/homework/upload", data, true, callback);
    }

    function downloadHomework(callback) {
        var data;
        request("POST", "api/homework/download", data, true, callback);
    }

    return {
        userlogin: userlogin,
        createHomework: createHomework,
        listHomework: listHomework,
        uploadHomework: uploadHomework,
        downloadHomework: downloadHomework
    }
})();