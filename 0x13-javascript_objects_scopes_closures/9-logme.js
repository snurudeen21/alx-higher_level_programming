#!/usr/bin/node
/* print argument index and value */
let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count += 1;
};
