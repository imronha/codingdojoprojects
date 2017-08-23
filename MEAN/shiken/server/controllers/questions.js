var mongoose = require("mongoose");
var Question = mongoose.model("Question");

module.exports = {
    create: function(req, res){
        console.log(`inside create question: ${req.body.content}`)
        var question = new Question({
            content: req.body.content,
            answers: []
        });
        question.save().then((doc)=>{
            console.log(`saved a question ${doc.content}`)
            res.json(question);
        }).catch((doc)=>{
            console.log("inside the .catch")
            console.log(doc)
            res.json("false");
        })
    },

    all: function(req, res){
        console.log("inside question.js all()")
        Question.find({}).sort({createdAt:-1,updatedAt:"asc"}).exec(function(err, players){
            if(err){
                console.log("errors");
                res.json("false");
            }
            else{
                console.log(`returning all the questions`)
                res.json(players);
            }
        })
    },

    show: function(req, res){
        console.log(req.params._id);
        Question.find({_id: req.params._id}, function(error, question){
            if(error){
                console.log('Error');
            }else {
                console.log('Question Found!');
                // console.log(cat[0]);
                res.json(question);
            }
        })
    },
}
