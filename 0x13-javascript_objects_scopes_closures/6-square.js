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
        let charc = '';
        for (let x = 0; x < this.size; x++) {
          charc += c;
        }
        console.log(charc);
      }
    }
  }
}
module.exports = Square;
