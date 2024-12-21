#!/usr/bin/node
const fs = require('fs');
const contentA = fs.readFileSync(process.argv[2], 'utf8');
const contentB = fs.readFileSync(process.argv[3], 'utf8');
const contentC = contentA.concat(contentB);
fs.writeFileSync(process.argv[4], contentC, 'utf8');
