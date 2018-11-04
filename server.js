const express = require('express')
const app = express();


const server = app.listen(7000, function(){
  console.log(`Express running on PORT ${server.address().port}`);
});
var helper = require('./app.js');

app.get('/', function(req,res){
  res.send({message: "Wegman's Node.js Backend API!"})
  });


app.get('/getStores/:num', function(req,res){
  var num = req.params.num;
  helper.wegmans.getStores(num,function(stores){
    res.send({0 : stores});
  })
});

app.get('/getStores/:num', function(req,res){
  var num = req.params.num;
  helper.wegmans.getStores(num,function(stores){
    res.send({0 : stores});
  })
});

app.get('/searchProducts/:searchTerms', function(req,res){
  var searchTerms = req.params.searchTerms;
  helper.wegmans.searchProductRequest()
});
