<img src='https://i.imgur.com/hjrS1e6.jpg'>

# JavaScript Objects Lab

## Introduction

This lab provides an opportunity to practice working with JavaScript objects and arrays.

## Setup

- Create a new JS-based repl in [repl.it](https://repl.it)

- Title your repl **JS Objects Lab**.

## Deliverable

- This lab is a **DELIVERABLE**.

- Submit the link to your repl using the form specified in the class repo's README.

## Instructions

- Copy the code below into the repl that you created.

- Solve each exercise as described.

- Do not change any of the existing code.

## Hints

You'll have to "chain" as necessary to get to the properties that exist on nested objects.  For example, if you wanted to access the `formats` property within the `album1` object, you would have to do this `album1.albumDetails.formats`. 

## Exercises

```js
const album1 = {
  title: 'Talking Heads',
  albumDetails: {
    released: new Date('September 16, 1977'),
    label: 'Sire',
    formats: ['LP']
  }
};

// Exercise 1:  Update the title property of album1 from 'Talking Heads' to 'Talking Heads - 77', then assign that property to a variable named title




// Exercise 2: Assign the string 'Sire' nested within album1 to a variable named label




const album2 = {
  title: 'More Songs About Buildings and Food',
  albumDetails: {
    released: new Date('July 14, 1978'),
    label: 'Sire',
    formats: ['LP', '8-track']
  }
};

const album3 = {
  title: 'Fear of Music',
  albumDetails: {
    released: 'August 3, 1979',
    label: 'Sire',
    formats: ['Cassette']
  }
};

// Exercise 3: Access the string 'LP' from the formats array within album2 and add it to the end of the formats array within album3.




// Exercise 4:  Update the released property within album3 from a string into a Date object using that same string.
// Hint: Look at album2 to see how to create a Date object. 




const album4 = {
  title: 'Remain in Light',
  albumDetails: {
    released: new Date('October 8, 1980'),
    formats: ['Cassette', 'LP']
  }
};

// Exercise 5:  Add a property named label with the value 'Sire' to album4's albumDetails property




const album5 = {
  title: 'Little Creatures',
  albumDetails: {
    released: new Date('June 10, 1985'),
    labels: ['Sire', 'emi'],
    formats: ['CD', 'cassette', 'LP']
  }
};

// Exercise 6:  Replace the 'emi' element in the labels array within album5 with 'EMI'




const album6 = {
  title: 'True Stories',
  albumDetails: {
    released: new Date('October 7, 1986'),
    labels: ['Sire, EMI'],
    formats: ['CD', 'cassette', 'LP']
  }
};

// Exercise 7:  Assign the formats array within album6 to a variable named formats




const album7 = {
  title: 'Naked',
  albumDetails: {
    released: new Date('March 15, 1988'),
    labels: ['Sire', 'EMI'],
    formats: ['CD', 'cassette', 'LP']
  }
};

const talkingHeadsAlbums = [
  album1,
  album2,
  album3,
  album4,
  album5,
  album6,
  album7
];

// Exercise 8:  Using the above talkingHeadsAlbums array, assign the labels property within album5 to a variable named labels




// Exercise 9:  Using the above talkingHeadsAlbums array, assign the released property within album7 to the released property within album6




// Exercise 10:  Using the pre-defined variable named albumIdx below, assign the albumDetails object of the album located within the talkingHeadsAlbums array at the index represented by the value of albumIdx to a variable named albumDetails

let albumIdx = 4;




/********** Don't look below here **********/

console.log('Exercise 1:', title);
console.log('Exercise 2:', label);
console.log('Exercise 3:', album3.albumDetails.formats[1]);
console.log('Exercise 4:', album3.albumDetails.released.toLocaleDateString());
console.log('Exercise 5:', album4.albumDetails.label);
console.log('Exercise 6:', album5.albumDetails.labels[1]);
console.log('Exercise 7:', formats);
console.log('Exercise 8:', labels);
console.log('Exercise 9:', talkingHeadsAlbums[5].albumDetails.released.toLocaleDateString());
console.log('Exercise 10:', albumDetails);
```

## When ran, the console should show the following:

```
Exercise 1: Talking Heads - 77
Exercise 2: Sire
Exercise 3: LP
Exercise 4: 8/3/1979
Exercise 5: Sire
Exercise 6: EMI
Exercise 7: [ 'CD', 'cassette', 'LP' ]
Exercise 8: [ 'Sire', 'EMI' ]
Exercise 9: 3/15/1988
Exercise 10: {
  released: 1985-06-10T00:00:00.000Z,
  labels: [ 'Sire', 'EMI' ],
  formats: [ 'CD', 'cassette', 'LP' ]
}
```

## Additional Resources

- [MDN Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)

- [MDN Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
