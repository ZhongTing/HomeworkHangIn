function HomeworkAPI(api) {
    this.create = function (year, name, totalScore, callback) {
        var data = new FormData();
        data.append("year", year);
        data.append("name", name);
        data.append("totalScore", totalScore);

        api.request("POST", "api/homework/create", data, true, callback);
    };

    this.list = function (callback) {
        var data = {};

        api.request("GET", "api/homework/list", data, true, callback);
    };

    this.upload = function (homeworkId, file, callback) {
        var data = new FormData();
        data.append("homeworkId", homeworkId);
        data.append("file", file);

        api.request("POST", "api/homework/upload", data, true, callback);
    };

    this.download = function (homeworkId, errorCallback) {
        api.downloadFile("api/homework/download", {
            token: api.accessToken,
            homeworkId: homeworkId
        }, errorCallback)
    };

    return {
        create: this.create,
        list: this.list,
        upload: this.upload,
        download: this.download
    }
}