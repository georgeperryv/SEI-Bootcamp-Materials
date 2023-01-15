[Class Repo](https://git.generalassemb.ly/SEIR-7-25/class-work/tree/master/work/w11/d4/02-mern-shopping-cart-part-2)

```js
// NewOrderPage.jsx

...
/*--- Event Handlers --- */
async function handleAddToOrder(itemId) {
  // Baby step
  alert(`add item: ${itemId}`);
}

return (
  ...

```


💪 Practice Exercise - handleAddToOrder (5 minutes)

1. Pass this all the way down to MenuListItem component. 
2. Update the onClick to invoke handleClickOrder argument of menuItem.id
3. Clicking it will show tha mongoID for that item. 

<!-- Inside NewOrderPage.jsx -->
Answer: 
1. Our prop is the handleAddToOrder
2. pass it down to MenuListItem component.
```js
<MenuList 
  menuItems={}...
  handleAddToOrder={handleAddToOrder}
/>
```
Now we need to destructure that newly passed prop.
Hold down command and click MenuList
3. Inside src/components/MenuList/MenuList.jsx:
```js
// src/components/MenuList/MenuList.jsx
export default function MenuList({menuItems, handleAddToOrder})
```

4. Inside MenuListItem component
```js
// src/components/MenuList/MenuList.jsx
<MenuListItem
  key={item._id},
  menuItem={item},
  handleAddToOrder={handleAddToOrder}
/>
```

5. Now we have to go to MenuListItem component. Command + click MenuListItem
Inside src/components/MenuListItem/MenuListItem.jsx
```js
// src/components/MenuListItem/MenuListItem.jsx
export default function MenuListItem({menuItem, handleAddToOrder})
// it now has access to handleAddToOrder
```

STEP 1 DONE!

Step 2: 

1. Inside src/components/MenuListItem/MenuListItem.jsx, in the button...
```js
// src/components/MenuListItem/MenuListItem.jsx
// Could have been able to figure it out menuItem._id  with above code
// Don't pass the whole menuItem itself, just the ID!
        <button className="btn-sm" onClick={() => handleAddToOrder(menuItem._id)}>
          ADD
        </button>
```

Step 3: Verify by adding item id when button is clicked.
Are the ids for hamburger and hotdog different? 