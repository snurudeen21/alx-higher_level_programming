#!/usr/bin/node
/* a function that returns a number occurrence of a
 * number in a list */
exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      num += 1;
    }
  }
  return num;
};
