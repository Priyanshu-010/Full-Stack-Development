"use client";

import { useParams } from "next/navigation";
import React from "react";
import parisImg from "@/assets/paris.jpg";
import tokyoImg from "@/assets/tokyo.jpg";
import nyImg from "@/assets/new york.webp";
import Image from "next/image";

function Page() {
  const { city } = useParams();
  return (
    <div className="text-white mt-25 w-[50%]">
      {city} is a beautiful city
      {city === "Paris" && (
        <Image src={parisImg} alt="Paris Image" width={400} height={400} />
      )}
      {city === "Tokyo" && (
        <Image src={tokyoImg} alt="Tokyo Image" width={400} height={400} />
      )}
      {city === "NewYork" && (
        <Image src={nyImg} alt="NewYork Image" width={400} height={400} />
      )}
    </div>
  );
}

export default Page;
