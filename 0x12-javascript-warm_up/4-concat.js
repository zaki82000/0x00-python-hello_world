#!/usr/bin/node
function argv () {
  const arg = process.argv[2];
  const arg1 = process.argv[3];
  const formatword = ' is ';
  console.log(arg + formatword + arg1);
}
argv();
