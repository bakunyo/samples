var _ = require('underscore');

var array = [0, 1, 2, 3];

// _.each(array, function(i) { console.log(i); });

// _(array).each(function(i) { console.log(i); });

_.chain(array)
  .map(function(i) { return i + 1; })
  .filter(function(i) { return i % 2 === 0; })
  .each(function(i) { console.log(i); });
