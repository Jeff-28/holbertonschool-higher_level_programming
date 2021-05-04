#!/usr/bin/nodejs

const file = process.argv.slice(2);

const fs = require('fs');
fs.readFile(file[0], 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
