var express = require('express');
var app = express();

app.set('port', (process.env.PORT || 5000));

app.use('/', express.static('assets'));
app.get("/", function(req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
        fs.readFile('./assets/index.html', 'utf8', function (err,data) {
            res.end(data);
        });
});
// views is directory for all template files
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');

app.get('/', function(request, response) {
  response.render('pages/index');
});

app.listen(app.get('port'), function() {
  console.log('Node app is running on port', app.get('port'));
});
