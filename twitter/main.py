import post_tweet
import prettier
import markovify
import MeCab

mecab = MeCab.Tagger("-Owakati")
with open("data.txt") as f:
    text = f.read()
text_model = markovify.NewlineText(
    "\n".join(map(mecab.parse, text.split("\n")))
)
for i in range(5):
    draft = text_model.make_sentence()
    if draft:
        tweet = prettier.escape_output(draft)
        print(tweet)
post_tweet.tweet(tweet)
