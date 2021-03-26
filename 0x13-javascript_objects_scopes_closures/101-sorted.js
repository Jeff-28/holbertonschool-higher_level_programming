#!/usr/bin/nodejs

const dict = require('./101-data').dict;

const New = {};
for (const obj in dict) {
  if (New[dict[obj]] === undefined) {
    New[dict[obj]] = [];
  }
  New[dict[obj]].push(obj);
}
console.log(New);
