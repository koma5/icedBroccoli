const rdf = require('rdf');
var request = require('request');
request('http://marcoko.ch/', function (error, response, body) {
      console.log('error:', error);
      console.log('statusCode:', response && response.statusCode); 
      console.log('body:', body); 

    var graph = new rdf.Graph()
    rdf.parse(body);
});



