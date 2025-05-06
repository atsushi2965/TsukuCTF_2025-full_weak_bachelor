# TsukuCTF 2025 Writeup![TsukuCTF](http://tsukuctf.org/files/b68962efbbda8558e610a62585d6a630/logo.png "TsukuCTF")
by **full_weak_bachelor**, a Japanese student team from [full_weak_engineer](//youtube.com/@full-weak-engineer)

[<img src="http://github.com/atsushi2965.png" alt="@atsushi2965" width=64 height=64 title=Atsushi2965>](//github.com/atsushi2965)
[<img src="http://github.com/yuneko1127.png" alt="@yuneko1127" width=64 height=64 title="ゆう猫">](//github.com/yuneko1127)
[<img src="http://github.com/Nichi10p.png" alt="@Nichi10p" width=64 height=64 title=Nichi10p>](//github.com/Nichi10p)
[<img src="http://github.com/shion0503.png" alt="@shion0503" width=64 height=64 title="Shion_erqp">](//github.com/shion0503)

27th place of all, 8th place of Japanese students
<img src="Top 10 Teams_opaque-pil-oxi.png" alt="Top 10 Teams (of Japanese Students)" title="Top 10 Teams (of Japanese Students)">
## 自己紹介
### Atsushi2965
インターネットの皆さんこんにちは､Atsushi2965です｡picoCTFすら触った事の無い文字通り脆弱な情報工学生ですが､なんかアスースンさんに暫定リーダーを任されたので最後まで張り切りました｡運良く1000近くポイントを獲れて嬉しみに浸っている所です｡

### ゆう猫 (yuneko1127)
こんにちは。初めまして。ゆう猫([@yuneko1127](https://github.com/yuneko1127))です。TsukuCTFで初めてチームでオープンなCTFに参加したので、ついでにWriteupを書きます。CTF歴は、picoCTFの過去問などに手を出して、SecHack365期間中に内部で行われたCTFに少しだけ参加したくらいの初心者です。弱かったため、OSINTのmedium以下しか解けなかった。他のものにも挑んだので、writeupで復習したいと思ってます。

### Nichi10p
Nichi10pです。本業(?)は競技プログラマーですが、YouTubeの[脆弱エンジニアの日常](https://www.youtube.com/@full-weak-engineer)チャンネルで開催された[リアルトリリオンゲーム](https://www.youtube.com/watch?v=Rhf34cOgkzA)企画に乗っかって参加した SECCON CTF 13 をきっかけに、CTFにも手を出しはじめました。\
イベント型CTFは3回目の参加でした (2回目は picoCTF 2025) 。

### Shion_erqp (shion)
shionです。TsukuCTFは[SecHack365](https://sechack365.nict.go.jp/)から[生まれたCTF](https://xryuseix.hatenablog.com/entry/2021/09/15/000412)であり、X(旧Twitter)上で盛り上がっていたので、流れに乗って参加しました。今回は2度目の参加で、以前よりも問題の質・種類ともにより良くなっていたと感じました。運営の方々ありがとうございました。


## osint
### Casca (Atsushi2965)
写真の右側にあるらしい記念碑に書かれた｢式典の開催日｣を書く課題｡
1. 頂いた写真をGoogle画像検索

   1番目のサイト（ブログ）に **｢熱海市とカスカイス市｣** という小見出しを発見
2. ｢熱海 カスカイス 碑｣でGoogle画像検索

   あるサイトに記念碑がしっかり映っており､日付も見えました｡

完｡

### curve (Atsush2965)
違和感（カーブしたエスカレータ）の映った写真から､その場所のWebサイトを暴く問題｡これも先の問題に同様､Google画像検索すると建物名が直ぐ出てきました｡

完｡

### buildings (yuneko1127)
建築中の建物を含む町の写真から緯度経度を提出する課題でした。とりあえず、Google画像検索をすると、この写真が品川駅周辺であることがわかり、あとはストリートビューで適切な位置を探して終わりです。

### destroyed (Nichi10p)
[Telegramの投稿](https://t.me/etozp/19319)の写真に写った、戦争で破壊された学校を特定する課題です。\
投稿本文のウクライナ語を一語一語Google翻訳で英語に訳して、良さげな検索ワードを考えます。「学校」の意味と固有名詞をいい感じに含む гімназію Степненської громади (gymnasium Stepnenskaya communities) としました。これを duckduckgo.com で検索します。\
私の前に調べを進めていた @shion さんからの不正解報告を目grepで除いていくと https://zp.isuo.org/schools/view/id/830 が気になります。\
情勢のためかアクセスがブロックされるので [Web Archive](https:///web.archive.org/web/20220126043917/https://zp.isuo.org/schools/view/id/830) で閲覧 (@shion さんからの入れ知恵) し、Поштова адреса (Postal code) を入手します。\
Googleマップで周辺を見るとそれっぽい建物があるので、URL (https://www.google.com/maps/place/47°47'53.8%22N+35°18'40.4%22E/@47.7973071,35.3037427,1314m) から緯度・経度を得て、FLAGを構築すると、正解でした。

### rider (yuneko1127)
夜の街の写真からその位置を当てる課題でした。看板で目を引いて検索できそうだった、OTiというフライドチキン屋さんを検索し、地図上で探します。一度探したときは、範囲を絞りすぎて探せなくて諦めたのですが、@shionさんがこの辺だと思うので引き取ってくださいと言っていたので、引き取ってもう一度広域にして検索して、店舗の前を何店舗か確認して見つけました。点字ブロックがあったので、ない店はすぐに却下していたら、楽に見つけられました。街灯も映っていたのでそれを参考に位置を合わせて終了です。

### schnee (yuneko1127)
ぱっと見、ヨーロッパの雪山っぽい風景だなと思いながら探した課題です。buildingと同じように画像検索をして、移っている店の名前がわかるので、それを探してストリートビューで適切な位置を探して終了です。

### power (yuneko1127)
日本の遺跡であろうということが写真からよくわかります。とりあえず点字が映っているので、このような説明で説明文の一番上の文章はその遺跡の名前が書かれていることが多いので、図の下にある説明文の一番上を点字を入力して、日本語に翻訳するサイトで読みを確認して検索して、Google Mapで位置を確認して終了です。


## crypto
### PQC0 (Atsushi2965)
PQC（ポスト量子暗号）なる物を使った問題らしいです｡よく分かりませんがChatGPTに聞いてったら解けました｡
1. 頂いた出力テキストから
   ```plaintext
   -----BEGIN PRIVATE KEY-----
   (中略)
   -----END PRIVATE KEY-----
   ```
   を抄出して`priv-ml-kem-768.pem`に保存
2. ciphertext(hex)を`ciphertext.dat`に保存
   - pythonなら
     ```py
     ciphertext_hex = '83daaca5593e84b6b90264...'
     with open('ciphertext.dat', 'wb') as f:
         f.write(bytes.fromhex(ciphertext_hex))
     ```
   - shellなら
     ```console
     $ echo '83daaca5593e84b6b90264...' | xxd -r -p > ciphertext.dat
     ```
3. ```console
   > openssl pkeyutl -decap -inkey priv-ml-kem-768.pem -in ciphertext.dat -out recovered_shared.bin
   ```
4. ```py
   >>> from Crypto.Cipher import AES
   >>> from Crypto.Util.Padding import unpad
   >>> 
   >>> with open('recovered_shared.bin', 'rb') as f:
   ...     key = f.read()
   ...
   >>> with open('encrypted_flag.bin', 'rb') as f:
   ...     ct = f.read()
   ...
   >>> cipher = AES.new(key, AES.MODE_ECB)
   >>> pt = unpad(cipher.decrypt(ct), 16)
   >>> pt.decode()
   TsukuCTF25{}
   ```

### a8tsukuctf (Atsushi2965)
よく分かりませんが､`enc.py`を見ると､[ヴィジュネル暗号](//ja.wikipedia.org/wiki/ヴィジュネル暗号#数式でみる暗号化と復号)なる物が使われているらしいです｡\
但し､暗号文中`tsukuctf`だけ不変なんだそうですね｡

実はChatGPTに聞いただけなんですが､各文字に使われる鍵は

$$K_i=\begin{cases}\mathtt{key}\_i&i<\mathtt{len}\left(\mathtt{key}\right)\\\C_{i-L}&i\ge\mathtt{len}\left(\mathtt{key}\right)\end{cases}$$

となっており､（初期）鍵が分からなくても途中からは暗号文自体から復号できてしまうんだそうです｡

そして､`tsukuctf`だけ不変という事は､その時の鍵が`aaaaaaaa`ならば良いので､鍵長は8字と分かります｡

以上を基に､
```py
>>> ciphertext = "ayb wpg uujmz pwom jaaaaaa aa tsukuctf, hj vynj? mml ogyt re ozbiymvrosf bfq nvjwsum mbmm ef ntq gudwy fxdzyqyc, yeh sfypf usyv nl imy kcxbyl ecxvboap, epa 'avb' wxxw unyfnpzklrq."
>>> from string import ascii_lowercase
>>>
>>> # build cipher_without_symbols list
>>> c_list = [c for c in ciphertext if c in ascii_lowercase]
>>> n = len(c_list)
>>> # compute p_list with None for i<8
>>> p_list = [None] * n
>>> # compute p for i>=8
>>> for i in range(8,n):
...     p_val = (ord(c_list[i]) - ord(c_list[i - 8])) % 26
...     p_list[i] = chr(ord('a') + p_val)
... 
>>> # Now reconstruct plaintext including non letters
>>> plaintext = []
>>> idx = 0
>>> for c in ciphertext:
...     if c in ascii_lowercase:
...         if idx >= 8:
...             plaintext.append(p_list[idx])
...         else:
...             plaintext.append('?')
...         idx += 1
...     else:
...         plaintext.append(c)
... 
>>> ''.join(plaintext)
"??? ??? ??joy this problem or tsukuctf, or both? the flag is concatenate the seventh word in the first sentence, the third word in the second sentence, and 'fun' with underscores."
```

### xortsukushift (Nichi10p)
要するに、擬似乱数生成器 `xor_tsuku_shift` の出力値 (mod 3) を 294 連続で的中させることが目標です。\
手元で `xor_tsuku_shift` を動かして、出力値 (mod 3) を 1000 件ほど観察すると、長さ 280 で周期的に見えます。周期の発見は、テキストを範囲選択すると選択したテキストと同じ部分をまとめてハイライトしてくれる vscode の機能でがんばります。\
適当な数字を返すとその勝敗から勝てる数字を割り出せるので、これを 280 回繰り返して必勝パターンを構築します。構築できたら適当に投げ続けて FLAG ゲットです。\
やりとりをいい感じに print するスクリプトを書いて解くと、見ていて楽しいです。


## web
### len_len (shion)
以下のような問題ファイルが与えられました。
```js
function chall(str = "[1, 2, 3]") {
  const sanitized = str.replaceAll(" ", "");
  if (sanitized.length < 10) {
    return `error: no flag for you. sanitized string is ${sanitized}, length is ${sanitized.length.toString()}`;
  }
  const array = JSON.parse(sanitized);
  if (array.length < 0) {
    // hmm...??
    return FLAG;
  }
  return `error: no flag for you. array length is too long -> ${array.length}`;
}
```
入力値を`.replaceAll(" ", "")`でサニタイズした後の文字列の長さが0以下(`array.length`)になるとFlagがもらえるようです。
しかし、文字列の長さがマイナスになる値など存在しません。よく見ると、文字列の長さチェックは`array.length`で行われています。実は、JavaScriptの辞書型を用いることで`.length`を上書きすることが可能です。
```
"hoge".length  // 4
{'length': -1}.length  // -1
```
ということで次のようなcURLを叩いてFLAG取得しました
```
curl http://(省略) -d 'array={"length":-1}'
```
`TsukuCTF25{l4n_l1n_lun_l4n_l0n}`

### flash (Atsushi2965)
はい､これもChatGPTの力を御借りしました｡\
どうやら`seed`と`session_id`から各ラウンドの数字を求めているらしいので､アクセスしながらクッキーを取得して同じ計算を自分ですれば良い､という事だそうですね｡

`seed`はどうするのかって？　実は`seed.txt`はURL直で開けば見れる様になっていたんですね｡脆弱だな～！

### YAMLwaf (Atsushi2965)
此方､hardだったので無理かなぁと思いきや､根気良くChatGPTに聞いてみたら､なんと解けてしまいました｡
```console
$ curl -X POST 'http://challs.tsukuctf.org:50001' \
>      -H 'Content-Type: text/plain' \
>      -d $'%TAG !b! tag:yaml.org,2002:binary\n---\nfile: !b! ZmxhZy50eHQ='
```
こんな回避があったんですねぇ｡


## pwn
全く解けませんでしたorz


## 結び
### ゆう猫 (yuneko1127)
私は以上で解説を書いた分をチームに貢献できる点数としてflagを獲得しました。OSINTのCasca、curveも取り組んで解けましたが、遅かったです(この辺をちゃんと分担できているといいのだろうと思います)。またOSINTのdestroyed、hidden_wpath、easy_kernelも取り組んだのですが、解けませんでした。destroyedは解き切りたかったですね。今後とも、CTFに参加していきたいのでよろしくお願いします。

### Nichi10p
destroyed (OSINT) の詰めと xortsukushift (crypto) の全体をやりました。easy_kernel (pwn) や PQC1 (crypto) も解きたかったのですが、力及ばず……\
OSINT は気づいたらあらかた解かれていて、PQC0 (crypto) も `openssl` をこねこねして悩んでいる間に解かれていたので、みんな自信なさげな割につよいじゃないか！　と思いました。ありがとうございました😊

### Shion_erqp (shion)
今回は他メンバーの解くスピードが早く全く使い物になりませんでした…
最近DOM clobberingを学んでいたおかげで、`len_len`で2nd solveを獲得できたことだけがちっぽけな誇りです。
同メンバーのwriteupを見ると私の貢献も記述してくれて優しいメンバーだなと感動しました。
次はhard問をカッコよく解けるくらいの実力をつけて仲間に貢献したいです。頑張ります。
皆さん、ありがとうございました！

### Atsushi2965
なんか結果的に私が一番多く解いていました｡まぁ初心者も初心者なので簡単な物を率先して解くのは正しいっちゃ正しいんじゃないでしょうか｡

唯､ゆう猫さんも仰った通り､分担を考えていなかったのはリーダーとして不足だったと反省しております｡チームマネジメントが今後の私の課題ですね｡

にしても､私にも（ChatGPTの力使いまくって）解ける難易度で､チームワークも抜群だったので､とても楽しかったです｡今後も脆弱エンジニア学生部門に顔を出せたらという所存です｡

- - -

以上｡御披見賜り､ありがとうございました｡m(__)m
