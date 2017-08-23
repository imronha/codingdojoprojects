var mongoose = require("mongoose");
const path = require("path");

questions = require("./../controllers/questions.js");

module.exports = function(app){

    app.get("/all_questions", function(req, res){
        console.log("inside routes.js /all_questions")
        questions.all(req, res);
    })

    app.post("/new_question", function(req, res){
        console.log("inside the express routing /new_question")
        questions.create(req, res);
    })

    app.get("/question/:id", function(req,res){
        console.log("inside show question routes.js")
        questions.show(req,res);
    })

    app.all("*", (req,res,next)=>{
        res.sendFile(path.resolve("./public/dist/index.html"))
    });



}
