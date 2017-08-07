var express = require('express');
var session = require('express-session');
var app = express();
app.set('view engine', 'ejs');
app.use(session({secret: 'codingdojorocks'}));

app.get('/', function(request, response){
    // request.session.counter = 0;
    if (request.session.counter == undefined){
        request.session.counter = 0;
    }
    if (request.session.counter>=0){
        request.session.counter+=1;
    }
    response.render('index', {session: request.session.counter})
})

app.listen(8000, function(){
    console.log("Listening to port 8000.")
})
