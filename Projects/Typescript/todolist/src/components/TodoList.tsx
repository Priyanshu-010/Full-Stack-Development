import TodoItem from "./TodoItem"

interface Todo{
  id: string,
  text: string,
  completed: boolean,
  createdAt: number
}
const TodoList = ({todos}:{todos: Todo[]}) => {
 return (
    <div className="text-white flex flex-wrap gap-4 w-[70%]">
      {todos.map((todo) => (
        <div key={todo.id}>
          <TodoItem todo={todo} />
        </div>
      ))}
    </div>
 )
}

export default TodoList