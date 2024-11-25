#!/usr/bin/node

const fs = require('fs');

// Retrieve the file path from the first argument
const filePath = process.argv[2];

if (!filePath) {
  console.error('Error: No file path provided');
  process.exit(1);
}

// Read the file content in UTF-8
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
