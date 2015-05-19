var API = new(function () {
    var api = this;
    this.serverURL = "http://140.124.181.195:9000/HomeworkHangIn/";
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
                console.log(action, ":success");
                if (typeof (data) == "object")
                    console.log(action, "=>", data);
                else if (typeof (data) == "string" && data.length < 100)
                    console.log(action, "=>", data);
                else
                    console.log(action, "=>", "response done");

                if (callback)
                    callback(true, data);
            },
            error: function (data) {
                console.log(action, ":fail");
                if (callback)
                    callback(false, data.responseText);
            }
        });
    };

    this.downloadFile = function (action, data, errorCallback) {
        $.fileDownload(api.serverURL + action, {
            data: data,
            failCallback: function (responseHtml, url, error) {
                console.log(error);
            }
        })
    };

    return {
        user: new UserAPI(api),
        homework: new HomeworkAPI(api)
    }
});
