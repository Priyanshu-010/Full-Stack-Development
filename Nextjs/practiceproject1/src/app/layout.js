import { Poppins } from "next/font/google";
import "./globals.css";
import Navbar from "@/components/Navbar";

const poppins = Poppins({
  subsets:["latin"],
  weight:['400', '600'],
  display: 'swap'
})

export const metadata ={
  title: "Travel Guide Website",
  description: "Best Travel guidance for all the big and small places in the world your go to guide for tavels"
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body
        className={`${poppins.className} w-screen h-screen bg-black text-white`}
      >
        <Navbar />  
        {children}
      </body>
    </html>
  );
}
