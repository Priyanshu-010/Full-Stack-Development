import { connect } from "mongoose";

const mongodbUrl = process.env.MONGO_URI;
if(!mongodbUrl){
  throw new Error("Mongo DB URL not found.");
}

let cached = global.mongoose

if(!cached){
  cached = global.mongoose = {conn:null,promise:null}
}

const connectDb = async()=>{
  if(cached.conn){
    console.log("DB Connected")
    return cached.conn
  }

  if(!cached.promise){
    cached.promise =  connect(mongodbUrl).then((c)=>c.connection)
  }

  try {
    cached.conn = await cached.promise
    console.log("DB Connected First Time")
  } catch (error) {
    throw error
  }

  return cached.conn
}

export default connectDb