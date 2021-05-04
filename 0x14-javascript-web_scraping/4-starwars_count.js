#!/usr/bin/nodejs

const args = process.argv.slice(2);
const request = require('request');
request(args[0], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const dict = JSON.parse(body);
  const films = dict.results;
  let counter = 0;
  for (const film of films) {
    for (const url of film.characters) {
      if (url.slice(-4) === '/18/') {
        counter += 1;
      }
    }
  }
  console.log(counter);
});
