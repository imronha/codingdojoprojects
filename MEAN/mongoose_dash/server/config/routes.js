var mongoose = require('mongoose');
var Cat = mongoose.model('Cat');
var cats = require('../controllers/cats.js');

module.exports = function(app){
    app.get('/', function(req, res) {
        cats.home(req, res);
    })
    app.get('/cats/new', function(req, res) {
        res.render('add_cat');
    })

    app.post('/cats', function(req, res) {
        cats.create(req, res);
    })

    app.post('/cats/destroy/:id', function(req, res){
        cats.remove(req, res);
    })

    app.get('/cats/:id', function(req, res){
        cats.show(req, res);
    })
}
