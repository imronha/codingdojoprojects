var mongoose = require('mongoose');
var notes = require('./../controllers/notes')
var Note = mongoose.model('Note');

module.exports = function (app){
    app.get('/', function(req, res){
        Note.find({}, function(errors, all_notes){
            res.json(all_notes);
        })
    })
    app.post('/new', notes.new);
}
