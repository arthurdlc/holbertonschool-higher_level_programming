#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath) {
  console.error('Error: No file specified');
  process.exit(1);
}

// lire les contenue des fichier sous le format utf8
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});