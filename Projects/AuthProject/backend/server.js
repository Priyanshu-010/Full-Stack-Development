import express from "express";
import dotenv from "dotenv"
import userRoutes from "./routes/user.route.js"
import { connectDb } from "./config/db.js";

dotenv.config()

const app = express();
const PORT = process.env.PORT || 3000


app.get("/", (req,res)=>{
  res.send("Hello World")
})

app.use('/api/users', userRoutes)

connectDb()
app.listen(PORT, ()=>{
  console.log(`Server started at PORT ${PORT}`)
})