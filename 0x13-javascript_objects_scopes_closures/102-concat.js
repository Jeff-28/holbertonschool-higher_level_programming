#!/usr/bin/nodejs

const f1 = process.argv[2];
const f2 = process.argv[3];
const f3 = process.argv[4];

const fs = require('fs');

const data1 = fs.readFileSync(f1, 'utf-8');
const data2 = fs.readFileSync(f2, 'utf-8');
fs.writeFileSync(f3, data1 + data2);
