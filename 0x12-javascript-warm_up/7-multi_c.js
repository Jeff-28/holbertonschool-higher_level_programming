#!/usr/bin/nodejs

const arg = process.argv[2];

if (isNaN(arg)) {
  console.log('Missing number of ocurrences');
} else {
  for (let i = 0; i < arg; i++) {
    console.log('C is fun');
  }
}
