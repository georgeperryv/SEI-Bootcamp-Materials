import React from "react";
import "./ToDoListItem.css";

function ToDoListItem({item, index}) {
    return (

        <li className="ToDoListItem" style={{backgroundColor: index % 2 ? "lavender" : "plum"}}>
            <div className="flex-ctr-ctr">{index + 1}</div>
            {item}</li>
    );
}

export default ToDoListItem;