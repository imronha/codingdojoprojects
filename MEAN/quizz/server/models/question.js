// require mongoose
var mongoose = require('mongoose');
// create the schema
var QuestionSchema = new mongoose.Schema({
  content: String,
  correct: String,
  fake1: String,
  fake2: String
}, { timestamps: true});
// register the schema as a model
var Question = mongoose.model('Question', QuestionSchema);
