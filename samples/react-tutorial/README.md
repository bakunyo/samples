# React-Tutorial

https://facebook.github.io/react/docs/tutorial-ja-JP.html

### JSXシンタックス
- composable(組み立てられる)
- (XMLっぽい)JSXシンタックスは生JSにコンパイルされる
  - <CommentBox /> -> React.createElement({ ...
  - diaplayNameは変数名から自動的に付与されるっっぽい

### props
- this.props.xxx で親要素から渡された値が取得可能
- this.props.children ネストされた子要素(タグの中身)の値が取得可能

### state
- props -> 親の所有物であり、イミュータブル
- state -> コンポーネント自身が持つ、ミュータブルな状態(state)
- componentDidMount -> コンポーネントがレンダリングされた際、Reactが自動的に呼び出す
- setState -> 状態(state)を更新するためのメソッド。

### つづき
新しいコメントの追加 から
https://facebook.github.io/react/docs/tutorial-ja-JP.html#
