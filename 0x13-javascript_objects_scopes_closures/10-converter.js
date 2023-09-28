#!/usr/bin/node
/* convert base to num */
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
