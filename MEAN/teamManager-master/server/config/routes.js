var mongoose = require("mongoose");
const path = require("path");

players = require("./../controllers/players.js");


// Routes
// Root Request
module.exports = function(app){

    app.get("/allPlayers", function(req, res){
        console.log("inside routes.js /allPlayers")
        players.all(req, res);
    })

    app.post("/createPlayer", function(req, res){
        console.log("inside the express routing create player")
        players.create(req, res);
    })

    app.post("/updateStatus", function(req,res){
        console.log("inside updateStatus")
        players.updateStatus(req,res);
    })
    app.post("/deletePlayer", function(req,res){
        console.log("inside delete player route.js")
        players.destroy(req,res);
    })

    app.all("*", (req,res,next)=>{
        res.sendFile(path.resolve("./public/dist/index.html"))
    });



}
