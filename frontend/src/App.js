import React, { useEffect, useState } from "react";
import axios from "axios";

const TodoApp = () => {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState("");
  const [priority, setPriority] = useState("LOW");
  const [editId, setEditId] = useState(null);

  // Fetch all todos on component mount
  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = () => {
    axios
      .get("http://localhost:8000/todos")
      .then((response) => setTodos(response.data))
      .catch((error) => console.error("Error fetching todos:", error));
  };

  const addTodo = () => {
    const todoData = {
      description: newTodo,
      priority: priority,
    };
    console.log("Submitting TODO with data:", todoData);
    axios
      .post("http://localhost:8000/todos", todoData)
      .then(() => {
        fetchTodos(); // Refresh list after adding
        setNewTodo("");
        setPriority("LOW");
      })
      .catch((error) => console.error("Error adding todo:", error));
  };

  const updateTodo = (id) => {
    const updatedTodo = {
      priority: priority,
      description: newTodo,
    };
    axios
      .put(`http://localhost:8000/todos/${id}`, updatedTodo)
      .then(() => {
        fetchTodos(); // Refresh the list after updating
        setEditId(null); // Clear edit mode
        setNewTodo(""); // Reset new todo input
        setPriority("LOW"); // Reset priority to default
      })
      .catch((error) => console.error("Error updating todo:", error));
  };

  const deleteTodo = (id) => {
    axios
      .delete(`http://localhost:8000/todos/${id}`)
      .then(() => {
        fetchTodos(); // Refresh list after deleting
      })
      .catch((error) => console.error("Error deleting todo:", error));
  };

  return (
    <div>
      <h1>Todo List</h1>
      {todos.map((todo) => (
        <div key={todo.id}>
          {editId === todo.id ? (
            <>
              <input value={newTodo} onChange={(e) => setNewTodo(e.target.value)} placeholder="Edit todo description" />
              <select value={priority} onChange={(e) => setPriority(e.target.value)}>
                <option value="LOW">LOW</option>
                <option value="MODERATE">MODERATE</option>
                <option value="HIGH">HIGH</option>
              </select>
              <button onClick={() => updateTodo(todo.id)}>Save</button>
            </>
          ) : (
            <>
              {todo.description} - Priority: {todo.priority}
              <button
                onClick={() => {
                  setEditId(todo.id);
                  setNewTodo(todo.description);
                  setPriority(todo.priority);
                }}
              >
                Edit
              </button>
              <button onClick={() => deleteTodo(todo.id)}>Delete</button>
            </>
          )}
        </div>
      ))}
      {editId == null && (
        <div>
          <input value={newTodo} onChange={(e) => setNewTodo(e.target.value)} placeholder="Add a new todo" />
          <select value={priority} onChange={(e) => setPriority(e.target.value)}>
            <option value="LOW">LOW</option>
            <option value="MODERATE">MODERATE</option>
            <option value="HIGH">HIGH</option>
          </select>
          <button onClick={addTodo}>Add Todo</button>
        </div>
      )}
    </div>
  );
};

export default TodoApp;
