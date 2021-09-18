# はじめに

こんにちは、高校1年の[Akimasa_L][twitter]です。

最近の僕たちの学校のトレンドとして、1個下の中学3年の代から、高校の新しい科目「情報」が追加されるようになって、そのため僕たちの学校の教師も†新しい情報教育†のためにいろんなことをしています。たとえば、PythonでMeCabという形態素解析エンジン等を使用したプログラミングをやってみよう！みたいなプログラムもあります。

さて、今日は2021年9月18日で、ちょうど台風14号が直撃しています。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/388631/fb0c788a-0570-1fe3-b65d-a44e059fb421.png)

おかげで午前6時ごろに横浜市に大雨洪水警報が発令され、学校が休校になりました！！！

![ファイル_000.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/388631/1e8eb4ca-ff26-8a68-2c27-502199bfc44c.png)

> やった～～

(現在午後3時ですが外は雨は一切降っていません。朝のあの暴雨は一体何だったのでしょうか。)

そんなため、今日一日暇になってしまったため、今日は「TLから学ぶもろこしbot」を作りました。そこで、このbotを作るに当たり様々なことを知らべたのでまとめてみたいと思います。

## マルコフ連鎖

みなさんは時々このようなツイートを過去の自分のツイートから自動生成するようなものを見たことがあるかと思います。ここで使われているのが「マルコフ連鎖」というアルゴリズムになっています。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/388631/3a167dc8-e237-4e18-878a-0a320d4d0845.png)

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/388631/018f84d3-8c5c-5b5f-d486-1c38b2126e38.png)

### マルコフ連鎖とは？

ここの記事の説明がわかりやすいです。

<https://omedstu.jimdo.com/2018/05/06/マルコフ連鎖による文書生成/>

すっごくかんたんに説明すると、

「私はトマトが好きです。」や「私は休みが欲しいです。」などの文をそれぞれ単語ごとに分解して

![image.png](https://i.imgur.com/UpCKbNX.png)

「私→は」「は→トマト」「は→休み」「が→好き」「が→ほしい」
などのこの単語の次にはこの単語が来やすいだろう、という確率を保存しておいて、

![image.png](https://i.imgur.com/HleFiS0.png)

その確率に応じて次の単語を決めて文を生成するというものになっています。

Wikipediaにはもっと詳しく数学的な話なども乗っています。僕は全く理解していません。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/388631/c15589a3-d31d-3578-1081-f58560d42cb3.png)

<https://ja.wikipedia.org/wiki/マルコフ連鎖>

### 実際に使ってみる

こんなにも複雑なマルコフ連鎖ですが、世の中は便利なもので、`markovify`というマルコフ連鎖のPythonのライブラリがあり、なにも理解していない僕でもかんたんにお手軽にマルコフ連鎖を体験できるようになっています。

<https://github.com/jsvine/markovify>

このライブラリはもともとは英語の文章生成のために作られたもので、与えられた英文の訓練データをもとに文頭や句点などを認識して勝手に文章を生成してくれます。

<https://business.aidemy.net/ai-can/introduction-seikogakuin/>

そこでとりあえず、僕たちの情報の科目を担当してくださっている先生が書いてくださった文章をdeeplに突っ込んで英文を生成して、それをもとに新しい英文を作ってみました。

```py
import markovify
t = """
Our school has been introducing inquiry classes for several years, but there have been some issues.
First of all, although we are aware of the importance of statistics, we only cover the ...
... o learn about Python and what machine learning can do from an earlier stage.
"""
text_model = markovify.Text(t)
for i in range(5):
    print(text_model.make_sentence())
```

`markovify.Text(t)`で`t`をもとにしてデータを作り、make_sentence()でそれをもとに文を生成します。

> In order to learn Python, and that hints and answers can be learned online and came across the Aidemy website.
> The satisfaction level of theme setting presented by the students was extremely high.
> The satisfaction level of theme setting presented by the students was extremely high.
> I was attracted to this aspect of the students in the inquiry classes has gone up a notch.
> The satisfaction level of the importance of statistics, we only have that opportunity once a year.

結果はこのようになりました。おおよそそれっぽい文章ができています。

### 日本語でやってみる

しかしこれはdeeplで生成した英文で、名塩先生が書いた元の文ではありません。このままでは名塩先生に怒られてしまいますのでつぎは名塩先生が書いたもとの日本語で文を生成しようと思います。

しかし、日本語は英語と違って、単語がスペースで区切られていないため、単語ごとに区切る作業が必要となります。

ここでは、MeCabという形態素解析エンジンを用いて行いました。

<http://taku910.github.io/mecab/>

MeCabというのは、例えば

`人生をやめてTwitterをはじめよう！`

という文を入力したときに、

```txt
人生    名詞,一般,*,*,*,*,人生,ジンセイ,ジンセイ
を      助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
やめ    動詞,自立,*,*,一段,連用形,やめる,ヤメ,ヤメ
て      助詞,接続助詞,*,*,*,*,て,テ,テ
Twitter 名詞,一般,*,*,*,*,*
を      助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
はじめよ        動詞,自立,*,*,一段,未然ウ接続,はじめる,ハジメヨ,ハジメヨ
う      助動詞,*,*,*,不変化型,基本形,う,ウ,ウ
！      記号,一般,*,*,*,*,！,！,！
```

と文を単語に区切って、それぞれの単語の品詞や読み方などを出力してくれるシステムです。(すごい)

今回はこのように品詞分解する機能は使わずに、分かち書き(単語ごとにスペースで区切る)機能を使ってみます。

MeCabは、文字のencodingの関係でWindowsでやるとめちゃくちゃ文字化けするのでWSLのUbuntu上でやっています。

<https://github.com/SamuraiT/mecab-python3>

PythonでMeCabを利用する際にはこのmecabのラッパーライブラリを用いました。

<https://business.aidemy.net/ai-can/introduction-seikogakuin/>

さっきのこの記事からもう一度テキストを引っ張ってきて、それをMeCabに読み込ませます。

```py
import markovify
import MeCab
mecab = MeCab.Tagger("-Owakati")
text="""
本校では数年前から探究の授業を導入していましたが、いくつか課題がありました。
まず統計についてはその重要性を認識しつつも、数学Iの授業で基礎を扱う程度に留まり、表計算を利用した実習...
...機械学習で出来ることについて学習の機会を設けていきたいと考えています。
"""
text_model = markovify.NewlineText(
    "\n".join(map(mecab.parse, text.split("\n"))))
for i in range(5):
    print(text_model.make_sentence())
```

このような感じで一行ずつ`mecab`で分かち書きしてそれを`markovify`でモデルを作ることによってこのような文章を生成できました。


> 教員 で ある 私 達 も 利用 し た と 感じ て い ます 。
> まず 統計 について は 、 大手 企業 様 を ゲスト に お 招き し て Python の 習得 は 将来 的 に も 必須 で ある 私 達 も 利用 し た と 感じ て い ます 。
> 生徒 たち の 満足 度 は 極めて 高い もの でし た ので 、 Aidemy Business の コンテンツ は 、 大手 企業 様 を ゲスト に お 招き し て い ます 。
> また 、 卒業生 に 依頼 し て Python の 導入 を 決意 し まし た 。
> まず 統計 について は 、 ブロック コーディング を 利用 する こと が でき ませ ん でし た 。

意味はあまり良くわかりませんが、いいかんじに文章が生成できています。

## 「TLから学んで学ぶもろこしbot」

これらのプログラムを使って、最後に「TLから学んで学ぶもろこしbot」を作りました。TLのツイートを学習データとして新しいツイートを生成します。勝手にメンションや画像をツイートされたら困るのでそれらはデータから削除しています。

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/388631/4899fc80-ed38-f847-9ace-4d1de6d8ea5c.png)

今回書いたソースコードはここに載せています。

<https://github.com/akimasa-l/morokoshi-bot>

# さいごに

台風で学校が休校になって暇になったのでTLから学ぶもろこしbotを作った話を書きました。短いコードでここまでできるのはすごいですね。それではよい3連休を！

[twitter]:https://twitter.com/Akimasa_L