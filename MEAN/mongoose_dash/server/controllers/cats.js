var mongoose = require('mongoose');
var Cat = mongoose.model('Cat')
mongoose.Promise = global.Promise;

module.exports = {
    home: function(req, res){
        Cat.find({}, function(err, results){
        if(err) { console.log(err); }
            res.render('cats', { cats: results });
        });
    },
    show: function(req, res){
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
    },
    create: function(req, res){
        var cat = new Cat({name: req.body.name, breed: req.body.breed});
        cat.save(function(error){
            if(error){
                console.log('Error');
            }else {
                console.log('Cat added!');
                res.redirect('/');
            }
        })
    },
    remove: function(req, res){
        console.log(req.params.id);
        Cat.remove({_id: req.params.id}, function(error){
            if(error){
                console.log('Error');
            }else {
                console.log('Cat Removed!');
                res.redirect('/');
            }
        })
    }
}
