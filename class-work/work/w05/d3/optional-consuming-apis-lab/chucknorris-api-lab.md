<img src="https://i.imgur.com/294n16z.png">

# Consume a 3rd Party API Lab

## Requirements

- Implement the choice of category of the joke!

## Hints

- The list of categories is available at this endpoint:<br>`https://api.chucknorris.io/jokes/categories`

- Set the form's method attribute to `method="GET"` so that the selected category will be submitted as a query string (see below).

- "Build" the categories as radio inputs within the form. Setting the `name` attribute on the inputs to `category` will result in the selected category being submitted as a query string and available on the server as `req.query.category`.

<img src="https://i.imgur.com/nVr5KUi.png">
