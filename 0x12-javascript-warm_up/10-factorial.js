#!/usr/bin/nodejs

function fact (x) {
  if (isNaN(x) || x === 1) {
    return (1);
  } else {
    return (x * fact(x - 1));
  }
}
const arg = process.argv[2];

console.log(fact(parseInt(arg)));
