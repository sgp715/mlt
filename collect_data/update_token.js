var casper = require("casper").create({
    pageSettings: {
        //userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:23.0) Gecko/20130404 Firefox/23.0"
        loadImages: false,
        userAgent: 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
        }
    });

var fb = "https://www.facebook.com/"

casper.start(fb, function(){
    //this.echo("inital url: " + this.getCurrentUrl());
    //this.capture("initial.jpg");
});

var terminate = function() {
    this.echo("");
    this.echo("EXITING..").exit();
    this.echo("");
};

function parseToken(tokenUrl) {

    splitToken = tokenUrl.split('=');
    almostToken = splitToken[1];
    token = almostToken.split('&')[0];
    return token

}

var username = casper.cli.get(0);
var password = casper.cli.get(1);

casper.thenEvaluate(function(user, pass) {
        //this.echo(user);
        document.getElementById("email").value = user;
		document.getElementById("pass").value = pass;
        document.getElementById("loginbutton").children[0].click(); 
},  {
    user: username,
    pass: password
});

casper.then(function() {
    //this.echo("waiting and then capturing login page");
    //this.echo("old: " + this.getCurrentUrl());
    this.wait(6000);
    //this.echo("new: " + this.getCurrentUrl());
    //this.capture('click.jpg');
});


var url = "https://www.facebook.com/dialog/oauth?client_id=464891386855067&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=public_profile,user_about_me,user_activities,user_birthday,user_education_history,user_location,user_photos,user_relationship_details&response_type=token";

casper.thenOpen(url);

casper.then(function() {
    //this.echo("obtaining the token: ");
    var tokenUrl = this.getCurrentUrl();
    //this.echo("token url: " + tokenUrl);
    var token = parseToken(tokenUrl);
    this.echo(token);
    //this.echo("saving token to file");
});

casper.run(function(){
 //this.echo("FINISHED");
 this.exit();
});
