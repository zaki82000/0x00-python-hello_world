#!/usr/bin/node

const square = require('./5-square.js');

class Square extends square {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let n = 0; n < this.size; n++) {
        let char = '';
        for (let x = 0; x < this.size; x++) {
          char += c;
        }
        console.log(char);
      }
    }
  }
}
module.exports = Square;
