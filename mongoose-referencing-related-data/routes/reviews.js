const express = require('express');
const router = express.Router();

const reviewCtrl = require('../controllers/reviews');

// http://localhost:3000/movies/123/reviews
router.post("/movies/:id/reviews", reviewCtrl.create);

module.exports = router;