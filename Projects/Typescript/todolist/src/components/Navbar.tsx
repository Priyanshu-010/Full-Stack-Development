const Navbar = () => {
  return (
    <div className="w-full border-b border-sky-700 flex justify-between p-6 mb-6 bg-sky-500">
      <h1 className="font-bold text-4xl">
        Todo
      </h1>
      <button className="flex gap-2 border-2 border-solid  rounded p-2">
        Create
      </button>
    </div>
  );
};

export default Navbar;
