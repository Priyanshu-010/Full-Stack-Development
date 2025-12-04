"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import React from "react";

function Navbar() {
  const pathname = usePathname();
  return (
    <div className="w-full h-20 bg-white border rounded-b-xl flex justify-between items-center px-4 text-black fixed top-0">
      <div className="text-black font-bold text-2xl">🌏Travel Guide</div>
      <div>
        <ul className="flex gap-4 justify-center items-center">
          <Link href={"/"} className={pathname == "/" ? "text-blue-500" : ""}>
            <li>Home</li>
          </Link>
          <Link
            href={"/destination"}
            className={pathname == "/destination" ? "text-blue-500" : ""}
          >
            <li>Destinations</li>
          </Link>
          <Link
            href={"/contact"}
            className={pathname == "/contact" ? "text-blue-500" : ""}
          >
            <li>Contact</li>
          </Link>
        </ul>
      </div>
    </div>
  );
}

export default Navbar;
