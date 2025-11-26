interface Todo{
  id: string,
  text: string,
  completed: boolean,
  createdAt: Date
}
const TodoItem = ({todo}: {todo: Todo}) => {
  return (
    <div>TodoItem</div>
  )
}

export default TodoItem