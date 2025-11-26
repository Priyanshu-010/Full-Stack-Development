import { useState, type FormEvent } from 'react'

type CreateTodo = (text: string) => void

interface TodoFormProps{
  create: CreateTodo
}

const TodoForm = ({create}: TodoFormProps) => {
  const [text, setText] = useState("")

  const handleSubmit = (e: FormEvent<HTMLFormElement>)=>{
    e.preventDefault();
    if(!text.trim()) return;
    create(text.trim())
    setText("")
  }

  return (
    <div className="w-[30%] fixed top-50 left-2/3">
      <form
        className="flex flex-col  justify-center items-center gap-4 w-100 h-45 bg-sky-300 p-4 border border-gray-800 rounded-2xl m-8 text-3xl font-bold text-black"
        onSubmit={handleSubmit}
      >
        <input
          type="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Add a Todo"
          className="border border-gray-800 rounded-4xl p-4 w-full"
        />
        <button type="submit" className="border border-gray-800 rounded w-30  ">
          Add
        </button>
      </form>
    </div>
  )
}

export default TodoForm