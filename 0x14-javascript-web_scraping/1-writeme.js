#!/usr/bin/nodejs

const args = process.argv.slice(2);

const fs = require('fs');
fs.writeFile(args[0], args[1], err => {
  if (err) {
    console.error(err);
  }
});
