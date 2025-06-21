// type
// used to create type aliases

type Users = {
  id: number;
  name: string;
  email?: string; // optional property
};

const users: Users = {
  id: 1,
  name: "Alice",
};

// Objects

type Product = {
    name: string;
    price: number;
  };
  
// Union Types
type Status = "loading" | "success" | "error";

// Primitive Aliases
type ID = number;

// Function Types
type Greets = (name: string) => string;

const sayHellos: Greets = (name) => `Hello, ${name}`;

// Tuples
type Point = [number, number];

const p: Point = [10, 20];

// Extending types
type Persons = { name: string };
type Employees = Persons & { employeeId: number };

const emp: Employees = {
  name: "John",
  employeeId: 123,
};
