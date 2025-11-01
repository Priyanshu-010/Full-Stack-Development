console.log("Hello World")

function greet(person: string, date: string): void{
  console.log(`Hello ${person}, today is ${date}!`);
}

greet("Brendan", new Date().toDateString());
