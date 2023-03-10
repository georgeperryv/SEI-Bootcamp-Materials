var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser'); 
var session = require('express-session'); // for Oauth npm i express-session to use dependency
var passport = require('passport'); // must npm i passport to use dependency
var methodOverride = require('method-override');
var logger = require('morgan');
require('dotenv').config(); // for .env file
require('./config/database');
require('./config/passport');

var indexRouter = require('./routes/index');
var moviesRouter = require('./routes/movies');
var reviewsRouter = require('./routes/reviews');
var performersRouter = require('./routes/performers');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({extended: false}));
app.use(cookieParser());
app.use(methodOverride('_method'));

// to use the session above, must be below cookieParser
app.use(session({
    secret: process.env.SECRET,
    resave: false,
    saveUninitialized: true
}));

// configuration to initialize and use a session
app.use(passport.initialize());
app.use(passport.session());

app.use(function (req, res, next) {
    res.locals.user = req.user;
    next();
});


app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/movies', moviesRouter);
app.use('/', reviewsRouter);
app.use('/', performersRouter);

// catch 404 and forward to error handler
app.use(function (req, res, next) {
    next(createError(404));
});

// error handler
app.use(function (err, req, res, next) {
    // set locals, only providing error in development
    res.locals.message = err.message;
    res.locals.error = req.app.get('env') === 'development' ? err : {};

    // render the error page
    res.status(err.status || 500);
    res.render('error');
});

module.exports = app;
