#!/usr/bin/node

function multi () {
  const x = process.argv[2];
  if (x === undefined) {
    console.log('Missing number of occurrences');
  } else {
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  }
}
multi();
