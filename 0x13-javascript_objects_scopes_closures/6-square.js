#!/usr/bin/node
/* a square class that inherit from Rectangle */
const SquareInherit = require('./5-square');

const square = class Square extends SquareInherit {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let i = 0; i < this.width; i++) {
        s += c;
      }
      console.log(s);
    }
  }
};
module.exports = square;
