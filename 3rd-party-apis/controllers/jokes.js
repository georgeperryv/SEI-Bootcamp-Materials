const fetch = require('node-fetch');
const rootAPIURL = 'https://api.chucknorris.io/jokes/random';

function getJoke(req, res) {
    fetch(rootAPIURL)
        .then(function (result) {
            console.log(result)
            return result.json();
        }).then(function (result) {
        console.log(result);
        return res.render(
            'index', {
                title: 'Chuck Jokes',
                result: result
            }
        );
    }).catch(function (error) {
        console.log(`error ${error}`);
    }).finally(function () {
        console.log('runs no matter what!');
    })
}

module.exports = {
    getJoke
}