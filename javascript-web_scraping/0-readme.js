#!/usr/bin/node

const fs = require('fs');

// trouver le chemin du fichier a lire si ce dernier existe
const filePath = process.argv[2];

if (!filePath) {
  console.error('Error: No file path provided');
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