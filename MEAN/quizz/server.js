var express = require('express');
var path = require('path');
var app = express();

require('./server/config/mongoose.js');

require('./server/config/routes.js')(app);

// app.use(express.static(__dirname + '/public/dist'));
// app.use(express.static(path.join(__dirname, '/public/dist')));
app.set('views', path.join(__dirname, 'public/dist'));

app.listen(8000, function() {
    console.log("listening on port 8000");
})
