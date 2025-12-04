"use client"

import { useRouter } from "next/navigation";
import React from "react";

function Page() {
  const destination = ["Paris", "Tokyo", "Mumbai"];
  const router = useRouter();
  return (
    <div className="flex justify-center items-center text-white h-full flex-col gap-4">
      <div className="text-3xl font-bold">Choose Your Destination</div>
      <div className="flex flex-col gap-6">
        {destination.map((d, idx) => (
          <div
            key={idx}
            className="font-bold text-2xl text-black flex  items-center justify-center rounded-2xl w-50 h-25 bg-white cursor-pointer hover:opacity-[0.5] transition-all"
            onClick={()=>router.push(`/destination/${d}`)}
          >
            {d}
          </div>
        ))}
      </div>
    </div>
  );
}

export default Page;
