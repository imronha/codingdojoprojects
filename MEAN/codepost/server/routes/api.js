const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');


var Cat = mongoose.model('Cat');
var cats = require('../controllers/cats.js');


mongoose.Promise = global.Promise;
