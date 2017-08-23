const mongoose = require('mongoose');
const Question = mongoose.model('Question');

module.exports = (function(){
    return {
        new: function(req, res){
            var question = new Question({content: req.body.content, correct: req.body.correct, fake1: req.body.fake1, fake2: req.body.fake2});
            question.save((errors, results) => {
                console.log(results);
                if (errors){
                    console.log(errors);
                    res.end();
                } else {
                    res.json({question: question})
                    res.redirect('/');
                }
            })
        }
    }
})();
