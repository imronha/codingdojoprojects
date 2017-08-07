var express = require('express');
var path = require( "path");
var session = require('express-session');
var app = express();
var bodyParser = require('body-parser');

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));
app.use(session({secret: 'codingdojorocks'}));
app.use(express.static(path.join(__dirname + "./static")));

// app.use(express.static(__dirname + "/static"));
// app.set('views', __dirname + "/views");
app.use(bodyParser.urlencoded({extended: true}));

app.get('/', function(request, response){
    response.render('index');
})

app.post('/users', function(request, response){
    info = request.body;
    console.log(request.body);
    response.render('index', info)
})

var server = app.listen(8000, function() {
    console.log("listening on port 8000");
});
var io = require('socket.io').listen(server);

io.sockets.on('connection', function (socket) {
    // console.log(socket);
    console.log("Client/socket is connected!");
    console.log("Client/socket id is: ", socket.id);
    // all the server socket code goes in here
    socket.on("posting_form", function (data){
        console.log(data);
        var lucky_num = Math.floor((Math.random()*1000)+1);
        socket.emit('message', {response: data});
        socket.emit('lucky_num', {response: lucky_num});
    })

})
