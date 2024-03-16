#!/usr/bin/node
/* using map to create a new Array */
const Arr = require('./100-data').list;

const newArr = Arr.map((x, index) => x * index);
console.log(Arr);
console.log(newArr);
