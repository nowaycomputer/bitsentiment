const MongoClient = require('mongodb').MongoClient
const express = require('express')
const bodyParser = require('body-parser')
const app = express()
var db

app.set('view engine', 'ejs')
app.use(bodyParser.urlencoded({extended:true}))


// MongoClient.connect('mongodb://bit:sentiment@ds017736.mlab.com:17736/bitsentiment', function(err,database){
// 	if (err) return console.log(err)
// 	db=database
// 	app.listen(3000, function(){
// 		console.log('listening on 3000')
// 	})
// })

MongoClient.connect('mongodb://localhost:27017/test', function(err,database){
	if (err) return console.log(err)
	db=database
	app.listen(3000, function(){
		console.log('listening on 3000')
	})
})

app.get('/', function(req,res){
	// Get the last 10 stories
	db.collection('bitsentiment').find({'type': 'news_story'}).limit(10).sort({_id:-1}).toArray(function(err,result){
		if (err) return console.log(err)
		res.render('index.ejs',{quotes: result})
	})
})

app.post('/quotes', function(req,res){
	db.collection('quotes').save(req.body, function(err,result){
		if (err) return console.log(err)
		console.log('saved to database')
		res.redirect('/')
	})
})


