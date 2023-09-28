#!/usr/bin/node
/* return a list in reverse order */
exports.esrever = function (list) {
  const rev = [];
  for (let i = list.length - 1; i >= 0; i--) {
    rev.push(list[i]);
  }
  return rev;
};
