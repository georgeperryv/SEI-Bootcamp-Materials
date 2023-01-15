# SEI Week 11 Quiz - Answer Key

## Promises, Fetch and Async/Await

### (1) What will the following async function `helloWorld` always return when invoked?

  ```js
  async function helloWorld() {
    return 'hello world!';
  }
  ```

  #### Solution

  ```
  A promise.
  Note: The promise in this case will resolve to the string 'hello world'
  ```


### (2) What two arguments can be provided to the `fetch(arg1, arg2)` function?

  #### Solution

  ```
  arg1 --> the URL/path/endpoint of the request
  arg2 --> the optional "options" object used to configure the request
  ```

### (3) What does the promise returned by `fetch()` resolve to?

  #### Solution

  ```
  An object that represents the response
  ```

## `useEffect` and `useRef`

### (4) What is the first argument we provide to the useEffect hook?

  #### Solution

  ```
  A callback function that contains the code we want useEffect to run
  ```

### (5) If no second argument is provided to the `useEffect` hook, when does the callback function run?

  #### Solution

  ```
  After every render
  ```

### (6) If we pass an empty array as the second argument to the useEffect hook, when does the callback function run?

  #### Solution

  ```
  After the first render only
  ```

### (7) Is the use case of `useRef` more similar to that of `useState` or `useEffect`?

  #### Solution

  ```
  useState because useRef is used to remember a value (like useState) whereas useEffect is for running code after a render
  ```

## Mongoose

### (8) A ________ property on a Mongoose schema is a "computed" property that is not actually saved in the document.

  #### Solution

  ```
  virtual
  ```

### (9) We can add custom _________ methods callable on a Mongoose model (hint: a model is a class).

  #### Solution

  ```
  static
  'class' is also acceptable
  ```

### (10) What Mongoose model query method should we use to find a single document that belongs to a certain user and isn't paid?

  #### Solution

  ```
  findOne
  ```