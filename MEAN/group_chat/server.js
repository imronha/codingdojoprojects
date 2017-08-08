const express = require('express');
const app = express();
const path = require( "path");

app.set('view engine', 'ejs');
app.set('views', (__dirname + "/views"));
app.use(express.static(path.join(__dirname + "./static")));

app.get('/', function(request, response){
    response.render('index')
})

const server = app.listen(8000, function(){
    console.log("Listening to port 8000.")
})

const io = require('socket.io').listen(server);
var users = [];
var messages = [];

io.sockets.on('connection', function (socket) {
    // console.log(socket);
    console.log("Client/socket is connected!");
    console.log("Client/socket id is: ", socket.id);
    socket.emit("chatroom_history", {users: users, messages: messages})

    socket.on("get_name", function(data){
        users.push({name: data.name, id: socket.id})
    })
    socket.on("msg_sent", function(data){
        console.log("Submitted! Msg: "+data.content);
        var sender;
        for (var i =0; i< users.length; i++){
            if (users[i].id == socket.id) {
                sender = users[i].name;
            }
        }
        console.log("sender:"+sender);
        messages.push({content: data.content, name: sender})
        io.emit("distribute_msg", {content: data.content, name: sender})
    })
    socket.on('disconnect', function(){
        console.log("Someone disconnected")
        for (var i =0; i< users.length; i++){
            if (users[i].id == socket.id) {
                console.log("found")
                users.splice(i,1);
            }
        }
    })
})

// setInterval(function(){
//     console.log(users);
//     console.log(messages);
// }, 2000);
