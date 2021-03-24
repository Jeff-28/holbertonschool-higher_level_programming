#!/usr/bin/nodejs

exports.esrever = function (list) {
  const rev = [];
  for (let i = 0, j = list.length - 1; i < list.length; i++, j--) {
    rev[i] = list[j];
  }
  return (rev);
};
