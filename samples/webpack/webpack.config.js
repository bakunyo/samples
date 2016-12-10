class MyWebpackPlugin {
  apply(compiler) {
    compiler.plugin('compile', (params) => {
      console.log('compile開始時の処理')
    })

    compiler.plugin('compilation', (compilation, params) => {
      // compilationもまたpluginメソッドを持つので、各イベントに処理を挿し込める
      compilation.plugin('optimize', () => {
        console.log('optimize(最適化)開始時の処理')
      })
    })

    // 非同期(async)に実行されるイベントはcallbackを引数で受取り、適宜実行する
    compiler.plugin('emit', (compilation, callback) => {
      console.log('emit(アセット出力)開始時の処理')
      callback()
    })
  }
}

module.exports = {
  entry: "./entry.js",
  output: {
    path: __dirname,
    filename: "bundle.js"
  },
  module: {
    loaders: [
      { test: /\.css$/, loader: "style!css" }
    ]
  },
  plugins: [
    new MyWebpackPlugin()
  ]
};
