#!/usr/bin/node

const fs = require('fs');

// Function to read and print file content
function printFileContent (filePath) {
  // Read file asynchronously
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
}
const filePath = process.argv[2];
// Call the function to print file content
printFileContent(filePath);
