var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var session = require('express-session');

app.get('/', function(request, response){
    response.send("<h1>Hello Express</h1>");
})

app.listen(8000, function(){
    console.log("Listening to port 8000.")
})

app.use(session({secret: 'codingdojorocks'}));
app.use(express.static(__dirname + "/static"))
app.set('views', __dirname + "/views");
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));

app.get('/users', function (request, response){
    var users_array = [
        {name: "Mike", email: "mike@test.com"},
        {name: "Jay", email: "jay@test.com"},
        {name: "Cat", email: "c@test.com"},
        {name: "Pup", email: "pup@test.com"},
    ];
    response.render('users', {users: users_array});
})

app.post('/users', function (req, res){
    console.log("POST DATA \n\n", req.body)
    req.session.name = req.body.name;
    console.log(req.session.name);
    //code to add user to db goes here!
    // redirect the user back to the root route.
    res.redirect('/')
});

app.get("/users/:id", function (req, res){
    console.log("The user id requested is:", req.params.id);
    // just to illustrate that req.params is usable here:
    res.send("You requested the user with id: " + req.params.id);
    // code to get user from db goes here, etc...
});
