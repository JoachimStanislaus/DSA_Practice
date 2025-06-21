// interface
// used to define the shape of an object

interface User {
  readonly id: number; // readonly prevents changes
  name: string;
  email?: string; // optional property
}

const user: User = {
  id: 1,
  name: "Alice",
  email: "alice@example.com",
};

// Interfaces can define function types:

interface Greet {
  (name: string): string;
}

const sayHello: Greet = (name) => `Hello, ${name}`;

// Extending Other Interfaces

interface Person {
  name: string;
}

interface Employee extends Person {
  employeeId: number;
}

const e: Employee = {
  name: "John",
  employeeId: 123,
};

// You can implement an interface in a class:
// The "implements" keyword in TypeScript is used to enforce that a class adheres to an interface.
interface Animal {
  name: string;
  speak(): void;
}

class Dog implements Animal {
  name = "Fido";
  speak() {
    console.log("Woof!");
  }
}
