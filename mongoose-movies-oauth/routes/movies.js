const express = require('express');
const router = express.Router();
const moviesCtrl = require('../controllers/movies');
const isLoggedIn = require('../config/auth');

router.get('/', moviesCtrl.index);
router.get('/new', moviesCtrl.new);
router.get('/:id', isLoggedIn, moviesCtrl.show);
router.post('/', isLoggedIn, moviesCtrl.create);

module.exports = router;
