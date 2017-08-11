var mongoose = require('mongoose');
var express = require('express');
var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.set('views', (__dirname + "/client/views"));
app.set('view engine', 'ejs');

mongoose.Promise = global.Promise;

mongoose.connect('mongodb://localhost/quotes_db');
var CatSchema = new mongoose.Schema({
    name: String,
    breed: String
})
mongoose.model('Cat', CatSchema);

require('./server/config/mongoose.js');

var routes_setter = require('./server/config/routes.js');
routes_setter(app);

// Setting our Server to Listen on Port: 8000
app.listen(8000, function() {
    console.log("listening on port 8000");
})
