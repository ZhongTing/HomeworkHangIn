function UserAPI(api) {
    this.login = function (account, password, callback) {
        var data = {
            account: account,
            password: password
        };
        api.request("POST", "api/user/login", data, false, function (success, data) {
            if (success) {
                api.accessToken = data.accessToken;
                console.log("AccessToken:", api.accessToken);
            }
            callback(success, data);
        });
    };

    return{
        login: this.login
    }
}