#!/usr/bin/node
const Arr = require('./100-data').list;
const newArr = list.map(function (x, index) {
  return x * index;
});

console.log(Arr);
console.log(newArr);
