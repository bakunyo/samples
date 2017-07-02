# アクターモデル
- アクター = プロセス
- ただし、OSのプロセスとはまったくの別物

# プロセスの処理
- spawn
  - プロセスを生成。
  - PIDが返る
- receive
  - メッセージを待ち受ける。1度だけ実行される。
  - プロセスを維持したい場合は、処理の最後で自分自身を呼び出す。
- send

## リンク
- spawn_link でリンクしつつ生成
- リンクはプロセス間相互監視
- Process.exit(pid, "reason") で終了
- 終了シグナルを受信しても終了しないプロセスを「システムプロセス」と呼ぶ
- システムプロセスにするには Process.flag(:trap_exit, true) をCall

## モニタ
- リンクと違い、一方的に監視するのがモニタ
- spawn_monitor は pid だけでなく reference も返す
  - { pid, ref } = spawn_monitor(SampleFunc, :hello2, ["山田"])
- リンクと違い、監視先が終了しメッセージを受信してもプロセスが終了しない


# ErlangとOTP
- Erlangでは、プロセスの操作として抽象化された処理やパターンがOTP(Open Telecom Platform)というフレームワークとして提供されている。
- 両者は密接に結びついているので、 Erlang/OTP と総称する場合もある。
- OTPのパターンは、ビヘイビアと呼ばれる

## GenServer
- OTPのビヘイビアのひとつ
- クライアント／サーバー処理における振る舞いを抽象化
- `use GenServer` のようにModuleに定義すればインポートできる



