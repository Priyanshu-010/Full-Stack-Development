import { PlusIcon } from "lucide-react";
import { Link } from "react-router-dom";
const Navbar = () => {
  return (
    <div className="w-full border-b border-sky-700 flex justify-between p-6 mb-6 bg-sky-500">
      <Link to='/' className="font-bold text-4xl">Todo</Link>
      <button className="flex gap-2 border-2 border-solid  rounded p-2">
        Create <PlusIcon />
      </button>
    </div>
  );
};

export default Navbar;
