var express = require('express');
var routes = require('./routes');
var user = require('./routes/user');
var http = require('http');
var path = require('path');

// Mongo Database stuff
var mongo = require('mongodb');
var monk = require('monk');
var db = monk('localhost:27017/demo');

var app = require('express.io')();
app.http().io();

// Setup the ready route, join room and broadcast to room.
app.io.route('ready', function(req) {
    req.io.join(req.data)
    req.io.room(req.data).broadcast('announce', {
        message: 'New client in the ' + req.data + ' room. '
    })
})

app.io.route('hello', function(req) {
    console.log('hello!');
})

// Send the client html.
app.get('/', function(req, res) {
    res.sendfile(__dirname + '/login.html')
})

app.listen(7076);