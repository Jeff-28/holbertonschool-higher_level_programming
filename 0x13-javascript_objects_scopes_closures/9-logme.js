#!/usr/bin/nodejs

let x = 0;
exports.logMe = function (item) {
  console.log(`${x}: ${item}`);
  x++;
};
