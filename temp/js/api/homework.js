function HomeworkAPI(api) {
    this.create = function (year, name, totalScore, callback) {
        var data = {
            year: year,
            name: name,
            totalScore: totalScore
        };
        api.request("POST", "api/homework/create", data, true, callback);
    };

    this.list = function (callback) {
        var data = {};
        api.request("GET", "api/homework/list", data, true, callback);
    };

    this.upload = function (callback) {
        // http://stackoverflow.com/questions/5392344/sending-multipart-formdata-with-jquery-ajax
        var data;
        api.request("POST", "api/homework/upload", data, true, callback);
    };

    this.download = function (callback) {
        var data;
        api.request("POST", "api/homework/download", data, true, callback);
    };

    return {
        create: this.create,
        list: this.list,
        upload: this.upload,
        download: this.download
    }
}