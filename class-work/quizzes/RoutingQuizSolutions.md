# Routing Quiz Solutions

Use the Routing Guide as necessary...
Assume a data resource of cats when answering the following:

1. What will the name of the router module be? (include its parent directory)
```
routes/cats.js
```

2. Write the line of code within server.js that would require the above router and assign it to a variable named catsRouter.
```js
var catsRouter = require('./routes/cats');
```

3. Write the line of code within server.js that would mount the above router object prefixing the proper path.
```js
app.use('/cats', catsRouter);
```

Using the router object within routes/cats.js and assuming a cats controller assigned to a variable named catsCtrl:

4. Write the line of code that defines the proper route that would read/display all cats (cats index route).
```js
router.get('/', catsCtrl.index);
```

5. Write the line of code that defines the proper route that would read/display a single cat (cats show route).
```js
router.get('/:id', catsCtrl.show);
```

Using the router object within routes/cats.js and assuming a cats controller assigned to a variable named catsCtrl:

6. Write the line of code that defines the proper route that would display a view that includes a form for submitting a new cat (cats new route).
```js
router.get('/new', catsCtrl.new);
```

7. Write the line of code that defines the proper route that would handle the cat form being submitted and creates a new cat (cats create route).
```js
router.post('/', catsCtrl.create);
```
