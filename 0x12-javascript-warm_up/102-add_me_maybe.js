#!/usr/bin/nodejs

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
