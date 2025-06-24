class Animal {
  name: string; // Type enforced
}

class Dog {
  private secret: string = "barks at night";

  revealSecret() {
    console.log(this.secret);
  }
}

// Access modifiers
// public – default; accessible everywhere
// private – accessible only inside the class, subclasses cannot access it but they inherit it
// protected – accessible inside the class and its subclasses

// Inheritance
class Animals {
  move() {
    console.log("Moving...");
  }
}

class Bird extends Animals {
  fly() {
    console.log("Flying...");
  }
}

const b = new Bird();
b.move(); // Inherited from Animal
b.fly();

// Implements

// Define an interface
interface Animal {
  name: string;
  speak(): void;
}

// Class implementing the interface
class Dogs implements Animal {
  name: string;

  constructor(name: string) {
    this.name = name;
  }

  speak() {
    console.log("Woof!");
  }
}
