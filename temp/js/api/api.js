var API = new (function () {
    var api = this;
    this.serverURL = "http://140.124.181.195:9000/"
    this.accessToken = "";

    this.request = function (type, action, data, needAccessToken, callback) {
        $.ajax({
            type: type,
            url: api.serverURL + action,
            cache: false,
            contentType: false,
            processData: false,
            beforeSend: function (request) {
                if (needAccessToken)
                    request.setRequestHeader("Authorization", api.accessToken);
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
    };

    return {
        user: new UserAPI(api),
        homework: new HomeworkAPI(api)
    }
});