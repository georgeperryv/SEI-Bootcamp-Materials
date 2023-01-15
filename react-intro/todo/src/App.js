import './App.css';
import ToDoList from "./ToDoList";
import {useState} from "react";
import NewToDoForm from "./NewToDoForm";

function App() {
    // const todoArray = [
    //     'Have Fun',
    //     'Learn React',
    //     'Learn the MERN-Stack'
    // ];

    // const [name, setName] = useState("Suresh");
    const [todos, setTodos] = useState([
        'Have Fun',
        'Learn React',
        'Learn the MERN-Stack'
    ]);

    const [showTodos, setShowTodos] = useState(true);

    function addTodo(newTodo) {
        console.log("The new value is " + newTodo);
        setTodos([...todos, newTodo]);
    }

    return (
        <div className="App">
            <h1>React To-Do</h1>
            <button onClick={() =>
                setShowTodos(!showTodos)}>
                {showTodos ? 'HIDE' : 'SHOW'}
            </button>
            {showTodos && <ToDoList todos={todos}/>}
            <hr/>
            <NewToDoForm addTodo={addTodo}/>
        </div>
    );
}

export default App;
