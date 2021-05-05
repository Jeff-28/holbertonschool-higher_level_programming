#!/usr/bin/nodejs

const args = process.argv.slice(2);
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/', function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const dict = JSON.parse(body);
  const films = dict.results;
  const id = 'https://swapi-api.hbtn.io/api/films/' + args[0] + '/';
  for (const film of films) {
    if (film.url === id) {
      for (const url of film.characters) {
        request(url, function (err, response, body) {
          if (err) {
            console.error(err);
          }
          const character = JSON.parse(body);
          console.log(character.name);
        });
      }
      break;
    }
  }
});
