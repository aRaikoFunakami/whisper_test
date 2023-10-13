# whisper_test

Macの場合
```terminal
$ python3 app_whisper_test.py
$ open http://127.0.0.1:8080
```

# Hark
https://github.com/otalk/hark

無音時間が一定時間続いた場合に録音処理を終了するために利用した。

node.js 向けのソースコードをブラウザで利用できるように変換する
```terminal
$ browserify hark.js -o hark.bundle.js
```

ブラウザで hark という関数で呼び出せるように修正
```diff
- module.exports = function(stream, options) {
+ window.hark = module.exports = function(stream, options) {
```

# その他
- [マイクアイコンの取得先](
https://icooon-mono.com/12443-%e3%83%9e%e3%82%a4%e3%82%af%e3%81%ae%e3%83%95%e3%83%aa%e3%83%bc%e3%82%a2%e3%82%a4%e3%82%b3%e3%83%b3%e3%81%9d%e3%81%ae21/)