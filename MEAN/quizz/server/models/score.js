// require mongoose
var mongoose = require('mongoose');
// create the schema
var ScoreSchema = new mongoose.Schema({
  name: String,
  score: Number,
}, { timestamps: true});
// register the schema as a model
var Score = mongoose.model('Score', ScoreSchema);
