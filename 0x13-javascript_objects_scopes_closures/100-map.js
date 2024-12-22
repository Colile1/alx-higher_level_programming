#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const list = list.map(function (num, index) {
  return num * index;
});

console.log(list);