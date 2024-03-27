#!/usr/bin/node

const fs = require('fs');

function writeinFile (filePath, data) {
  fs.writeFile(filePath, data, (err) => {
    if (err) throw err;
  });
}
const filePath = process.argv[2];
const data = process.argv[3];
writeinFile(filePath, data);
