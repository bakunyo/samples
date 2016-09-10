var AssetsPlugin = require('assets-webpack-plugin');
var assetsPlugin = new AssetsPlugin();

entries = {
  application: './es2015/application',
  application2: './es2015/application2'
}

webpack_configs = Object.keys(entries).map(function(key) {
  return {
    context: __dirname + '/source',
    entry: { [key]: this[key] },
    output: {
      path: __dirname + '/distribution/javascript',
      filename: '[name]-[hash].js'
    },
    module: {
      loaders: [
        { 
          test: /\.js$/,
          exclude: /node_modules/,
          loader: 'babel',
          query: {
            presets: ['react', 'es2015']
          }
        }
      ]
    },
    plugins: [ new AssetsPlugin() ]
  }
}, entries);

module.exports = webpack_configs
