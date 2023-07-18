#!/usr/bin/node
/* create a class Rectangle */
const rectangle = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
module.exports = rectangle;
