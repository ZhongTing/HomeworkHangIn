var currentUser = (function () {

    var account, role, token;

    function init(data) {
        account = data.account;
        role = data.role;
        token = data.accessToken;
    }

    function isTa() {
        return role !== "Student";
    }

    function getToken() {
        return token;
    }

    return {
        init: init,
        isTa: isTa,
    }
})();
