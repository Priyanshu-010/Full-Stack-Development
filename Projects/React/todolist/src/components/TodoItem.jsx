import React, { useState } from 'react'

const TodoItem = ({todo}) => {
  const [checked, setChecked] = useState(false)
  return (
    <div className='card bg-sky-300 border border-gray-800 min-h-45 w-55 text-black font-semibold text-2xl text-wrap flex items-center gap-4 justify-between p-4 rounded-2xl '>
      <p className={checked ? `line-through` : ``}>{todo.text}</p>
      <input type="checkbox" defaultChecked= {checked} onChange={(e) => setChecked(e.target.checked)} className='w-6 h-4'/>
    </div>
  )
}

export default TodoItem