#!/usr/bin/nodejs

const args = process.argv.slice(2);
const fs = require('fs');
const request = require('request');
request(args[0], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  fs.writeFile(args[1], body, err => {
    if (err) {
      console.error(err);
    }
  });
});
