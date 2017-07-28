var inbox = require("inbox");
var util = require("util");
var addrparser = require('address-rfc2822');

var client = inbox.createConnection(false, "", {
    secureConnection: false,
    auth: {
        user: "",
        pass: ""
    }
});
client.connect();
client.on("connect", function () {
    client.openMailbox("INBOX", function (error, info) {
        if (error) throw error;

        client.listMessages(-1, function (err, messages) {
            messages.forEach(function (message) {
                console.log(message.title+ 
                    util.inspect(addrparser.parse(client.createMessageStream(4).pipe(process.stdout, {end: false}))));
            });
        });

    });
});
client.on("new", function (message) {
    console.log("New incoming message ");
    console.log(message.UID + ": " + message.title);
});