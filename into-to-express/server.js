// here we load the express web framework
const express = require('express');
const path = require('path');

// we import the getAll method from
// todo-db.js module
const todoDb = require('./data/todo-db');

const contactUsData = require('./data/contact-us-data');

// here we create the express app
const app = express();

// we tell the express that we're going to use
// ejs as our templating system
app.set('view engine', 'ejs');

// tell the express the location of the
// views folder
app.set('views', path.join(__dirname, 'views'));

// here we create the url path
// http://www.suresh.com/home
// http://localhost/home
app.get('/', function (req, res) {
    res.render('home');
})

// http://localhost/todos
app.get('/todos', function (req, res) {
    // we render the template
    res.render('todos/index', {
        name: "Suresh",
        language: "Java",
        data: todoDb.getAll()
    });
});


// http://localhost:3000/contact-us
app.get('/contact-us', function (req, res) {
    res.render('contact-us/index', {
        data: contactUsData
    });
});


// http://www.myapp.com/admin/getusers/
// http://www.myapp.com/admin/createuser/
// http://www.myapp.com/admin/updateuser/
// http://www.myapp.com/admin/deleteuser/


// this is the starting point for the server
app.listen(3000, function () {
    console.log("Listening on port 3000");
});