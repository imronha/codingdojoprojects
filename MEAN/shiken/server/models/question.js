var mongoose = require("mongoose");

var QuestionSchema = new mongoose.Schema({
    content: {
        type: String,
        required: true,
        minlength:2
    },
    answers: [
        {response:"", likes: 0}
    ]
}, {timestamps:true});

var Question = mongoose.model("Question", QuestionSchema);
