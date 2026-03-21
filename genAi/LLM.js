import { GoogleGenAI } from "@google/genai";
import dotenv from "dotenv";
dotenv.config();

const ai = new GoogleGenAI({apiKey: process.env.GOOGLE_API_KEY});

async function main() {
  const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: [
      {
        role: 'user',
        parts:[{text: 'Hi, I am priyanshu'}]
      },
      {
        role: 'model',
        parts:[{text: "Hello Priyanshu! It's nice to meet you."}]
      },
      {
        role: "user",
        parts: [{text: "What is my name?"}]
      },
      {
        role: "model",
        parts: [{text: "Your name is Priyanshu."}]
      },
      {
        role: "user",
        parts: [{text: "what is your name?"}]
      },
    ]
  });
  console.log(response.text);
}

await main();