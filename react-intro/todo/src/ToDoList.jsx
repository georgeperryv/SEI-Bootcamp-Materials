import React from "react";
import ToDoListItem from "./ToDoListItem";
import "./ToDoList.css";

function ToDoList({todos}) {
    return (
            <ul className="ToDoList">
                {
                    todos.map((value, index) =>
                        <ToDoListItem key={index} item={value} index={index}/>
                    )
                }
            </ul>
    )
}

export default ToDoList;