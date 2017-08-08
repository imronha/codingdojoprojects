const express = require('express');
const app = express();

app.set('view engine', 'ejs');
app.set('views', (__dirname + "/views"))

app.get('/', function(request, response){
    response.render('index')
})

const server = app.listen(8000, function(){
    console.log("Listening to port 8000.")
})

const io = require('socket.io').listen(server);

io.sockets.on('connection', function (socket) {
    let count = 0;

    // console.log(socket);
    console.log("Client/socket is connected!");
    console.log("Client/socket id is: ", socket.id);
    // all the server socket code goes in here
    socket.on("button_pressed", function (){
        count++;
        console.log(count);
        io.emit("update_count", count)
    })
    socket.on("reset_count", function (){
        count = 0;
        io.emit("update_count", count)
    })

})
