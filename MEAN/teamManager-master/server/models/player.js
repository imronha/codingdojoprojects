var mongoose = require("mongoose");

var playerSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        minlength:2
    },
    position:{
        type: String,
        required: true,
        minlength:2
    },
    status:{
        type:[String]
    }
}, {timestamps:true});

var Player = mongoose.model("Player", playerSchema);