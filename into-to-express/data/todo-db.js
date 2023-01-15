const todos = [
    {title: 'Feed Dogs', done: true},
    {title: 'Learn Express', done: false},
    {title: 'Buy Milk', done: false}
];

module.exports = {
    getAll: function () {
        return todos;
    }
};