import TodoItem from "../components/TodoItem";

const TodoList = ({ todos }) => {
  return (
    <div className="text-white flex flex-wrap gap-4 w-[70%]">
      {todos.map((todo) => (
        <div key={todo.id}>
          <TodoItem todo={todo} />
        </div>
      ))}
    </div>
  );
};

export default TodoList;
