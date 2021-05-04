#!/usr/bin/nodejs

const args = process.argv.slice(2);
const request = require('request');
request.get(args[0], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log('code:', response.statusCode);
});
