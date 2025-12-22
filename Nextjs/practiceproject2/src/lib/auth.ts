import { NextAuthOptions } from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import connectDb from "./db";
import User from "@/model/user.model";
import bcrypt from "bcryptjs";

const authOptions:NextAuthOptions = {
  providers:[
    CredentialsProvider({
      name:"Credentials",
      credentials:{
        email:{label: 'Email',type:'text'},
        password:{label: 'Password',type:'Password'}
      },
      async authorize(credentials, req) {
        const email = credentials?.email
        const password =  credentials?.password
        if(!email ||  !password){
          throw new Error("Email or Password not found")
        }
        await connectDb();
        const user = await User.findOne({email})
        if(!user){
          throw new Error("User not found")
        }

        const isMatch = await bcrypt.compare(password,  user.password)
        if(!isMatch){
          throw new Error("Incorrect Password")
        }

        return {
          id: user._id,
          name: user.name,
          email: user.email,
          image: user.image
        }
      },
    })
  ],
  callbacks:{

  },
  session:{

  },
  pages:{

  },
  secret:"my_secret"
}
export default authOptions;