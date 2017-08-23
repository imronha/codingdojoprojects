const mongoose = require('mongoose');
const Note = mongoose.model('Note');

module.exports = (function(){
    return {
        new: function(req, res){
            var note = new Note({text: req.body.text});
            note.save((errors, results) => {
                console.log(results);
                if (errors){
                    console.log(errors);
                    res.end();
                } else {
                    res.json({note: note})
                    res.redirect('/');
                }
            })
        }
    }
})();
