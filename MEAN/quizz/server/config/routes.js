var mongoose = require('mongoose');
var questions = require('./../controllers/questions')
var Question = mongoose.model('Question');

module.exports = function (app){
    app.get('/', function(req, res){
        Question.find({}, function(errors, all_questions){
            res.json(all_questions);
        })
    })
    app.post('/new', questions.new);
}
