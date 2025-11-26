import { useState } from "react"
import TodoList from "../components/TodoList"
import TodoForm from "../components/TodoForm"

interface Todo{
  id: string,
  text: string,
  completed: boolean,
  createdAt: Date
}
const Home = () => {
  const [todos, setTodos] = useState<Todo[]>([])


  return (
    <div className="flex items-center justify-between">
      <TodoList todos={todos}/>
      <TodoForm />
    </div>
  )
}

export default Home