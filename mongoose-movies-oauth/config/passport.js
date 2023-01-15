// is a general dependency for different oauth authentications
const passport = require('passport');
// need to specify which oauth to use
const GoogleStrategy = require('passport-google-oauth').OAuth2Strategy
const User = require('../models/user');

passport.use(
    new GoogleStrategy(
        // Configuration object
        {
            clientID: process.env.GOOGLE_CLIENT_ID,
            clientSecret: process.env.GOOGLE_SECRET,
            callbackURL: process.env.GOOGLE_CALLBACK
        },
        // The verify callback function
        function(accessToken, refreshToken, profile, cb) {
            // a user has logged in with OAuth... 
            User.findOne({googleId:profile.id}).then(async function(user) {
                // check if user exists, if so don't do anything but return user info
                if (user) return cb(null, user);
                try{
                    //info from google documentation
                    user = await User.create({
                        name: profile.displayName,
                        googleId: profile.id,
                        email: profile.emails[0].value,
                        avatar: profile.photos[0].value
                    });
                } catch (error) {
                    return cb(error);
                }
            })    
        }
    )
);

// serializer is called after the verify callback function when a user logs in
passport.serializeUser(function(user, cb) {
    //returns the nugget of data that passport is going to add to the session used to track user
    cb(null, user._id);
})

//this method is called every time a req comes from existing loggin in user
passport.deserializeUser(function(userId, cb) {
    User.findById(userId).then(function(user) {
        cb(null, user);
    });
});
