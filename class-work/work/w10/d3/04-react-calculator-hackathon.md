<img src="https://i.imgur.com/9LPuJgJ.jpg">

# React Calculator Hackathon

## Intro

Hackathons are events, usually hosted by a tech company, where programmers team up to collaborate for a short period of time on a project.

Hackathons can be a competitive event with prizes awarded to the winning team(s).

Hackathons are a great learning experience and provide an opportunity to meet others and network.

## Assignment

Each team will work to code a calculator app in React that looks and works like the basic calculator built into the Mac:

<img src="https://i.imgur.com/PcwwhLN.png">

After time is up, each team will have an opportunity to show how close their calculator is to that of the above goal. Do NOT expect to be able to completely finish coding the calculator's behavior - just do as much as you can.

Unlike during the early development phase of most applications where we prioritize the behavior over styling, in this hackathon, prioritize rendering a beautiful UI using a component hierarchy that looks like the above calculator over implementing all of the calculator's behavior.

## Setup

One team member needs to create a React sandbox in [codesandbox.io](https://codesandbox.io/).

All sandboxes by default allow for [live collaboration](https://codesandbox.io/docs/live) - just click the [Share] button, click the [Copy Sandbox Link] and share it with all teammates.

## Hints and Suggestions

### Fundamental Philosophy of React Frontend Programming

The following is fundamental to every React application:

- **We code components to render (visualize) application-state**, e.g., render a `<ToDoListItem>` component for each to-do in the `todos` application-state array.
- **We can code components to render other components based upon UI-state**, e.g., hide/show a component based upon `showDetails` UI-state, or disable a button based upon `isValid`, etc.
- **In response to user-interaction, we apply any necessary program logic and/or calculations and ultimately update all impacted state causing the components to re-render.**

### Workflow

- Use the [Live Collaboration Feature](https://codesandbox.io/docs/live) of CodeSandbox.
- Mob program (where everyone focuses on the same code at the same time) or break up responsibilities, e.g., defining certain components, defining state, layout/CSS, etc. 

### UI Layout, etc.

- [CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/) is the go to for laying out the calculator's UI.
- Since grid items (direct children of a Grid) are automatically laid out from left-to-right, top-to-bottom - rendering those React Elements in the correct order will be important.
- Make grid items span multiple columns by setting the `grid-column-start` & `grid-column-end` properties, or by using the `grid-column` shorthand property.
- Here are the characters for the math symbols:
  - `+`
  - `−`
  - `×`
  - `÷`
  - `=`
  - `%`
  - `±`

### Components

- Consider creating a component for the "display" and each type of "button". For example, you might create a:
  - `<Display>` component for displaying the current number being entered
  - `<Digit>` component for the `0`..`9` digits
  - `<Decimal>` component for the `.` (decimal point)
  - `<Operation>` component for the `+`, `−`, etc.
  - Etc.
- The above components and others would be are responsible for:
  - Rendering themselves.
  - Responding to being clicked which may include:
    - Invoking a function passed to it from `<App>`
    - If necessary, ignores the click in the handler function, e.g., when the decimal point is "pressed" and the current number being inputted already [includes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/includes) a decimal point.

### State

- There are several pieces of information that must be "remembered" as the user interacts with the calculator, for example:
  - The current number being entered. Hint: It might be easier to use a string for this state as the user is inputting it instead of a number. The string can then be converted to a number when stored as the first operand or used in a calculation (as the second operand).
  - The first operand entered prior to the user pressing an operation.
  - The selected math operation.
  - The result.

### Logic, etc.

- What the `<Display>` component renders would be based upon certain logic. For example, render the result state if it has a value (isn't `null`), otherwise render the current number state.
- Consider using a data structure for looking up the math operations, for example:

  ```jsx
  const OPERATIONS = {
    '+': (a, b) => a + b,
    '−': (a, b) => a - b,
    // etc.
  };
  ```

- Again, in response to user interaction (a "button has been clicked), we apply any necessary program logic and/or calculations and ultimately update all impacted state.  After stubbing up the event handler function, write comments for what you need to accomplish in plain language (pseudocode).

## Have Fun!

## More About Hackathons

Here are a couple of sites to check out if you're interested in participating in a hackathon:

- [hackathon.io](https://www.hackathon.io/events)

- [DEVPOST](https://devpost.com/hackathons)
