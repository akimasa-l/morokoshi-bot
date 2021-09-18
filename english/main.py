import markovify
with open("nashio.txt") as f:
    t = f.read()
text_model = markovify.Text(t)
for i in range(5):
    print(text_model.make_sentence())
