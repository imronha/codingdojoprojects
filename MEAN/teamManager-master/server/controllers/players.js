var mongoose = require("mongoose");
var Player = mongoose.model("Player");

module.exports = {
    create: function(req, res){
        console.log(`inside create player here's the stuff ${req.body.name}, ${req.body.position}, ${req.body.status}`)
       
        var player = new Player({
            name: req.body.name,
            position: req.body.position,
            status: req.body.status
        });
        player.save().then((doc)=>{
            console.log(`saved a player ${doc.name}`)
            res.json(player);
            console.log("after res.json before redirect")
        }).catch((doc)=>{
            console.log("inside the .catch")
            console.log(doc)
            res.json("false");
        })
    },

    all: function(req, res){
        console.log("inside players.js all()")
        Player.find({}).sort({createdAt:-1,updatedAt:"asc"}).exec(function(err, players){
            if(err){
                console.log("errors");
                res.json("false");
            }
            else{
                console.log(`returning all the players`)
                res.json(players);
            }
        })
    },
    updateStatus: function(req, res){
        console.log(`stuff from req.body = ${req.body.playerId}, ${req.body.status}, ${req.body.idx}`)
        console.log("inside players.js updateStatus");
        let player = new Player();
        console.log(player)
        let idx = req.body.idx;
        let setter = {};
        setter[`status.${idx}`]=req.body.status; //this line builds the query which is used in the line below as $set:setter... $set is followed by a querry of what key to match and what value to set it to. Because we want to use a variable in the key we have to build this query here first and pass it in as a whole.
        player = Player.findOneAndUpdate({_id:req.body.playerId},{$set:setter}, {new:true}, function(err, result){
            if(err){
                console.log(err);
                res.json(err);
            }
            else{
                console.log(result);
                player = result;
            }
        })
    },
    destroy: function(req, res){
        
        console.log("inside delete player controller")
        console.log(`the player id is ${req.body.playerId}`)
        Player.remove({_id:req.body.playerId}, function(err, result){
            if(err){
                console.log("failed to delete player")
                res.json(err);
            }
            else{
                console.log("deleted player")
                console.log(result.name)
                res.json("good job")
            }
        }).exec();
    }
}
