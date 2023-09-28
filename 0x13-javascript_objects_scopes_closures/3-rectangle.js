#!/usr/bin/node
/* create a class Rectangle */
const rectangle = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let i = 0; i < this.width; i++) {
        s += 'X';
      }
      console.log(s);
    }
  }
};
module.exports = rectangle;
