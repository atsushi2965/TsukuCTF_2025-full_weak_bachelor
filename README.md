# TsukuCTF 2025 Writeup![TsukuCTF](http://tsukuctf.org/files/b68962efbbda8558e610a62585d6a630/logo.png "TsukuCTF")
by **full_weak_bachelor**, a Japanese student team from [full_weak_engineer](//youtube.com/@full-weak-engineer)

[<img src="http://github.com/atsushi2965.png" alt="@atsushi2965" title="Atsushi2965" width="64px;" />](//github.com/atsushi2965)
[<img src="http://github.com/yuneko1127.png" alt="@yuneko1127" title="ゆう猫" width="64px;" />](//github.com/yuneko1127)
[<img src="http://github.com/Nichi10p.png" alt="@Nichi10p" title="Nichi10p" width="64px;" />](//github.com/Nichi10p)
[<img src="http://github.com/shion0503.png" alt="@shion0503" title="Shion_erqp" width="64px;" />](//github.com/shion0503)
## 自己紹介
### Atsushi2965

### ゆう猫 (yuneko1127)
こんにちは。初めまして。ゆう猫([@yuneko1127](https://github.com/yuneko1127))です。TsukuCTFで初めてチームでオープンなCTFに参加したので、ついでにWriteupを書きます。CTF歴は、picoCTFの過去問などに手を出して、SecHack365期間中に内部で行われたCTFに少しだけ参加したくらいの初心者です。弱かったため、OSINTのmedium以下しか解けなかった。他のものにも挑んだので、writeupで復習したいと思ってます。

### Nichi10p
Nichi10pです。本業(?)は競技プログラマーですが、YouTubeの[脆弱エンジニアの日常](https://www.youtube.com/@full-weak-engineer)チャンネルで開催された[リアルトリリオンゲーム](https://www.youtube.com/watch?v=Rhf34cOgkzA)企画に乗っかって参加した SECCON CTF 13 をきっかけに、CTFにも手を出しはじめました。\
イベント型CTFは3回目の参加でした (2回目は picoCTF 2025) 。

### Shion_erqp (shion)

## osint
### building(yuneko1127)
建築中の建物を含む町の写真から緯度経度を提出する課題でした。とりあえず、Google画像検索をすると、この写真が品川駅周辺であることがわかり、あとはストリートビューで適切な位置を探して終わりです。

### schnee(yuneko1127)
ぱっと見、ヨーロッパの雪山っぽい風景だなと思いながら探した課題です。buildingと同じように画像検索をして、移っている店の名前がわかるので、それを探してストリートビューで適切な位置を探して終了です。

### power(yuneko1127)
日本の遺跡であろうということが写真からよくわかります。とりあえず点字が映っているので、このような説明で説明文の一番上の文章はその遺跡の名前が書かれていることが多いので、図の下にある説明文の一番上を点字を入力して、日本語に翻訳するサイトで読みを確認して検索して、Google Mapで位置を確認して終了です。

### rider(yuneko1127)
夜の街の写真からその位置を当てる課題でした。看板で目を引いて検索できそうだった、OTiというフライドチキン屋さんを検索し、地図上で探します。一度探したときは、範囲を絞りすぎて探せなくて諦めたのですが、@shionさんがこの辺だと思うので引き取ってくださいと言っていたので、引き取ってもう一度広域にして検索して、店舗の前を何店舗か確認して見つけました。点字ブロックがあったので、ない店はすぐに却下していたら、楽に見つけられました。街灯も映っていたのでそれを参考に位置を合わせて終了です。

### destroyed (Nichi10p)
[Telegramの投稿](https://t.me/etozp/19319)の写真に写った、戦争で破壊された学校を特定する課題です。\
投稿本文のウクライナ語を一語一語Google翻訳で英語に訳して、良さげな検索ワードを考えます。「学校」の意味と固有名詞をいい感じに含む гімназію Степненської громади (gymnasium Stepnenskaya communities) としました。これを duckduckgo.com で検索します。\
私の前に調べを進めていた @shion さんからの不正解報告を目grepで除いていくと https://zp.isuo.org/schools/view/id/830 が気になります。\
情勢のためかアクセスがブロックされるので [Web Archive](https:///web.archive.org/web/20220126043917/https://zp.isuo.org/schools/view/id/830) で閲覧 (@shion さんからの入れ知恵) し、Поштова адреса (Postal code) を入手します。\
Googleマップで周辺を見るとそれっぽい建物があるので、URL (https://www.google.com/maps/place/47°47'53.8%22N+35°18'40.4%22E/@47.7973071,35.3037427,1314m) から緯度・経度を得て、FLAGを構築すると、正解でした。

## crypto
###


## web
###


## pwn
###


## 結び
### Atsushi2965

### ゆう猫 (yuneko1127)
私は以上で解説を書いた分をチームに貢献できる点数としてflagを獲得しました。OSINTのCasca、curveも取り組んで解けましたが、遅かったです(この辺をちゃんと分担できているといいのだろうと思います)。またOSINTのdestroyed、hidden_wpath、easy_kernelも取り組んだのですが、解けませんでした。destroyedは解き切りたかったですね。今後とも、CTFに参加していきたいのでよろしくお願いします。

### Nichi10p

### Shion_erqp (shion)

