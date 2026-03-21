import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({apiKey: "AIzaSyBoGGI_sDIRAMnojGYrq40qJ_0LnbiIRzc"});

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
      }
    ]
  });
  console.log(response.text);
}

await main();