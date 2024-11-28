#!/usr/bin/node

const fs = require('fs');

// Récupération des arguments depuis la ligne de commande
const filePath = process.argv[2];
const content = process.argv[3];

// Vérifier si les deux arguments nécessaires sont fournis
if (!filePath || content === undefined) {
  console.error('Usage: ./1-writeme.js <file_path> <string_to_write>');
  process.exit(1);
}

// Écriture dans le fichier en utf-8
fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
});
