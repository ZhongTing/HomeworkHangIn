var API = (function () {
    var api = this;
    this.accessToken = "";

    this.request = function (type, action, data, needAccessToken, callback) {
        $.ajax({
            type: type,
            url: "http://140.124.181.195:9000/" + action,
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
        user: (UserAPI)(api),
        homework: (HomeworkAPI)(api),
        createHomework: this.createHomework,
        listHomework: this.listHomework,
        uploadHomework: this.uploadHomework,
        downloadHomework: this.downloadHomework
    }
})();
