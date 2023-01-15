import React, {useState} from "react";

function NewToDoForm({addTodo}) {

    const [newTodo, setNewTodo] = useState("");

    function handleAddToDo(evt) {
        // alert(newTodo);
        evt.preventDefault();
        addTodo(newTodo);
        setNewTodo("");
    }

    return (
        <>
            <h2>New To-Do</h2>
            <form onSubmit={handleAddToDo}>
                <input value={newTodo}
                       onChange={(evt) => setNewTodo(evt.target.value)}
                       placeholder="New To-do"
                       required
                       pattern=".{4,}"
                />
                <button type="submit">ADD TO-DO</button>
            </form>
        </>
    )
}

export default NewToDoForm;