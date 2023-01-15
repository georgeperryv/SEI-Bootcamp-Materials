const User = require('../../models/user');
const jwt = require("jsonwebtoken");
const bcrypt = require("bcrypt");

function checkToken(req, res) {
    // req.user will always be there for you when a token is sent
    console.log('req.user', req.user);
    res.json(req.exp);
}

// http://localhost:3000/api/users
async function create(req, res) {
    try {
        const user = await User.create(req.body);
        const token = createJWT(user);
        res.json(token);
    } catch (err) {
        res.status(400).json(err);
    }
}

function createJWT(user) {
    return jwt.sign(
        // data payload
        {user},
        process.env.SECRET,
        {expiresIn: '24h'}
    );
}

async function login(req, res) {
    try {
        const user = await User.findOne({email: req.body.email});
        if (!user) throw new Error();
        const match = await bcrypt.compare(req.body.password, user.password);
        if (!match) throw new Error();
        const token = createJWT(user);
        res.json(token);
    } catch (err) {
        res.status(400).json('Bad Credentials');
    }
}

module.exports = {
    create,
    login,
    checkToken
};