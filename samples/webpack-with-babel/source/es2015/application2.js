import Person from './person';

class Friend extends Person {
  constructor(name) {
    super(name);
  }
  callName() {
    alert(this.name);
  }
}

var friend = new Friend('You');
console.log("test2");

friend.callName();
