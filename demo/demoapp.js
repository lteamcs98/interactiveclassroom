var express = require('express');
var routes = require('./routes');
var user = require('./routes/user');
var http = require('http');
var path = require('path');

// Mongo Database stuff
var mongo = require('mongodb');
var monk = require('monk');
var db = monk('localhost:27017/demo');
var users = db.get('usercollection');

var app = require('express.io')();
app.http().io();

// Setup the ready route, join room and broadcast to room.
app.io.route('ready', function(req) {
    req.io.join(req.data)
    req.io.room(req.data).broadcast('announce', {
        message: 'New client in the ' + req.data + ' room. '
    })
})

app.io.route('submit_message', function(req) {
    console.log('new message: ' + req.data);
    app.io.room('chat').broadcast('new_message', {
        message: req.data
    })
})


app.io.route('validate', function(req) {
    console.log('validating...');

    users.find({},{limit:20},function(e,docs){
        var found = false;
        for(var i = 0; i < docs.length; i++)
        {
            if(req.data == docs[i].username)
            {
                found = true;
            }
        }
        if(found)
        {
            console.log('successful login');
            req.io.respond({ message : 'successful login.', value: true });
            req.io.join('chat')
            req.io.room('chat').broadcast('new_message', {
                message: 'New client ' + req.data + ' in the chat room. '
            })
        }
        else 
        {
            console.log('failed login');
            req.io.respond({ message : 'login error.', value: false });
        }
    });
})

// Send the client html.
app.get('/', function(req, res) {
    res.sendfile(__dirname + '/index.html')
})

app.listen(7076);