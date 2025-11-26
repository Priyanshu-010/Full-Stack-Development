import { useState } from "react"
import TodoList from "../components/TodoList"
import TodoForm from "../components/TodoForm"

interface Todo{
  id: string,
  text: string,
  completed: boolean,
  createdAt: number
}
const Home = () => {
  const [todos, setTodos] = useState<Todo[]>([])

  const addTodo = (text:string)  =>{
    const newTodo: Todo ={
      id: crypto.randomUUID(),
      text,
      completed: false,
      createdAt: Date.now(),
    }
    setTodos((prev) =>[...prev, newTodo])
  }

  return (
    <div className="flex items-center justify-between">
      <TodoList todos={todos}/>
      <TodoForm create={addTodo}/>
    </div>
  )
}

export default Home