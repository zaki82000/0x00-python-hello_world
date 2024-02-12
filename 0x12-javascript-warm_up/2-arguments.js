#!/usr/bin/node

function countArgs () {
  return process.argv.length - 2;
}

const numArg = countArgs();

if (numArg === 0) {
  console.log('No argument');
} else if (numArg === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
