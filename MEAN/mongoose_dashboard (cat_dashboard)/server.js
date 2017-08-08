var mongoose = require('mongoose');
var express = require('express');
var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.set('views', (__dirname + "/views"));
app.set('view engine', 'ejs');

mongoose.Promise = global.Promise;

mongoose.connect('mongodb://localhost/quotes_db');
var CatSchema = new mongoose.Schema({
    name: String,
    breed: String
})
mongoose.model('Cat', CatSchema);
var Cat = mongoose.model('Cat')

app.get('/', function(req, res) {
    Cat.find({}, function(err, results){
    if(err) { console.log(err); }
        res.render('cats', { cats: results });
    });
    // res.render('cats');
})
app.get('/cats/new', function(req, res) {
    res.render('add_cat');
})

app.post('/cats', function(req, res) {
    console.log("POST DATA", req.body);
    // This is where we would add the user from req.body to the database.
    var cat = new Cat({name: req.body.name, breed: req.body.breed});
    cat.save(function(error){
        if(error){
            console.log('Error');
        }else {
            console.log('Cat added!');
            res.redirect('/');
        }
    })
})

app.post('/cats/destroy/:id', function(req, res){
    console.log(req.params.id);
    Cat.remove({_id: req.params.id}, function(error){
        if(error){
            console.log('Error');
        }else {
            console.log('Cat Removed!');
            res.redirect('/');
        }
    })
})

app.get('/cats/:id', function(req, res){
    console.log(req.params.id);
    Cat.find({_id: req.params.id}, function(error, cat){
        if(error){
            console.log('Error');
        }else {
            console.log('Cat Found!');
            console.log(cat[0].name);
            // console.log(cat[0]);
            res.render('show_cat', {cat: cat});
        }
    })
})

// Setting our Server to Listen on Port: 8000
app.listen(8000, function() {
    console.log("listening on port 8000");
})
