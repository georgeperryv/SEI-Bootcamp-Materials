const Movie = require('../models/movie');

function create(req, res){
    // comes from URL
    // console.log(req.params.id); 

    // comes from the form submisson
    // console.log(req.body);
    Movie.findById(req.params.id, function(error, movie){
        movie.reviews.push(req.body);
        movie.save(function(error){
            res.redirect(`/movies/${movie._id}`);
        });

    });
}

module.exports = {
    create,
}