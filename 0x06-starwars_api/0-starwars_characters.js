#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const mainUrl = 'https://swapi-api.alx-tools.com/api/films/';

const requestUrl = mainUrl + movieId;

request(requestUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const resp = JSON.parse(body);
  const characters = resp.characters;
  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.log(error);
      }
      const nameResponse = JSON.parse(body);
      console.log(nameResponse.name);
    });
  }
});
