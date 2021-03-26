#!/usr/bin/nodejs

const list = require('./100-data').list;

const newList = list.map(function (item, index, array) {
  return (item * index);
});

console.log(list);
console.log(newList);
