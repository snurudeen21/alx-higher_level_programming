#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map(function (x, index) {
  return x * index;
});

console.log(list);
console.log(newList);
