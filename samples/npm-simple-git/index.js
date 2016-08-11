var simpleGit = require('simple-git')( '/Users/bakunyo/workspace/samples' );

console.log('start simple git');

simpleGit.log(function(err, log) {
  console.log(log);
});
