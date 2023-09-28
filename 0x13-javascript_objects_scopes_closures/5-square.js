#!/usr/bin/node
/* a square class that inherit from Rectangle */
const Rectangle = require('./4-rectangle');

const square = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
module.exports = square;
