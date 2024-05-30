import MeCab

mecab = MeCab.Tagger()
with open("src/neko.txt", "r") as f, open("neko.txt.mecab", "w") as f2:
    lines = f.readlines()
    for text in lines:
        result = mecab.parse(text)
        f2.write(result)
