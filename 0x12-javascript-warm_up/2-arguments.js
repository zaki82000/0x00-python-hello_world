#!/usr/bin/node

function countArgs () {
  return arguments.length - 1;
}

const numArg = countArgs;

if (numArg === 0) {
  console.log('No argument');
} else if (numArg === 1) {
  console.log('Argument found"');
} else {
  console.log('Arguments found');
}
