const mongoose = require('mongoose');
const Score = mongoose.model('Score');

module.exports = (function(){
    return {
        new: function(req, res){
            var score = new Score({name: req.body.name, score: req.body.score});
            score.save((errors, results) => {
                console.log(results);
                if (errors){
                    console.log(errors);
                    res.end();
                } else {
                    res.json({score: score})
                    res.redirect('/');
                }
            })
        }
    }
})();
