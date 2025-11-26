import { useState } from 'react'
import TodoList from '../components/TodoList'
import TodoForm from '../components/TodoForm'

const Home = () => {
  const [todo, setTodo] = useState([]);
  const addTodo = (text)=>{
    const newTodo ={
      id: crypto.randomUUID(),
      text,
      completed: false,
      createdAt: Date.now(),
    }
    setTodo((prev)=> [...prev, newTodo])
  }

  return (
    <div className='flex items-center justify-between'>
      <TodoList todos={todo} />
      <TodoForm create= {addTodo}/>
    </div>
  )
}

export default Home