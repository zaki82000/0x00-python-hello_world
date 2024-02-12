#!/usr/bin/node

function argv () {
  const arg = process.argv[2];
  if (arg === undefined) {
    console.log('No argument');
  } else {
    console.log(arg);
  }
}
argv();
