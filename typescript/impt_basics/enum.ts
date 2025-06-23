// By default, members start at 0 and increment by 1.
// So, Direction.Up is 0, Direction.Down is 1, etc.

// Numeric Enums (Default behaviour)
enum Direction {
  Up, // 0
  Down, // 1
  Left, // 2
  Right, // 3
}

let move: Direction = Direction.Left;

console.log(move); // 2

// String Enums
enum Status {
  Loading = "LOADING",
  Success = "SUCCESS",
  Error = "ERROR",
}

let currentStatus: Status = Status.Success;

console.log(currentStatus); // "SUCCESS"


// More efficient form of enum - more optimised compile, compiles to let dir = 0;
const enum Directions {
  Up,
  Down,
  Left,
  Right,
}

let dir = Directions.Up;
