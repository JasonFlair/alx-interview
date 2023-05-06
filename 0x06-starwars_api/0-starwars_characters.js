#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const mainUrl = 'https://swapi-api.alx-tools.com/api/films/';

const requestUrl = mainUrl + movieId;

const resp = request(requestUrl, (error, response, body) => {
  if (error) console.log(error);
  return body;
});
console.log(resp);
