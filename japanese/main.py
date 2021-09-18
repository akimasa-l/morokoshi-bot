import markovify
import MeCab
mecab = MeCab.Tagger("-Owakati")
with open("nashio.txt") as f:
    text = f.read()
text_model = markovify.NewlineText(
    "\n".join(map(mecab.parse, text.split("\n"))))
for i in range(5):
    print(text_model.make_sentence())
