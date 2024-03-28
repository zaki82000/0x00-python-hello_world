#!/usr/bin/node
const request = require('request');
let count = 0;
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body).results;
    for (const film of json) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
}
);
