#!/usr/bin/node

const lang = 'C is fun';
let count = parseInt(process.argv[2]);

if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  while (count > 0) {
    console.log(lang);
    count--;
  }
}
