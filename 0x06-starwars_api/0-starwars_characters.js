#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const mainUrl = 'https://swapi-api.alx-tools.com/api/';

const requestUrl = mainUrl + 'films/' + movieId;

request(requestUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  resp = JSON.parse(body);
  characters = resp.characters;
  for (character of characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.log(error);
      }
      nameResponse = JSON.parse(body);
      console.log(nameResponse.name)
    })
  }
});
