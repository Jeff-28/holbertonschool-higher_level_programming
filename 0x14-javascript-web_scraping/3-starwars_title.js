#!/usr/bin/nodejs

const args = process.argv.slice(2);
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + args[0], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const dict = JSON.parse(body);
  console.log(dict.title);
});
