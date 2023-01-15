var express = require('express');
var router = express.Router();
const jokeCtrl = require('../controllers/jokes');

/* GET home page. */
router.get('/', jokeCtrl.getJoke);

module.exports = router;
