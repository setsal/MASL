import jieba
import jieba.analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import sqlite3
import nltk

jieba.set_dictionary("dict.txt.big.txt")
jieba.analyse.set_stop_words("stop_words.txt")

with open('test.txt', 'r') as f:
    input = f.read()

s = " "
seg_list = s.join(jieba.cut(input))
print(seg_list)
tags = jieba.analyse.extract_tags(input, 4)
print("\nkey word: \n")
print(s.join(tags))
print("\n")


word_list = jieba.lcut(input)
freq = nltk.FreqDist(word_list)
for key in freq:
    print(key, freq[key])


wc = WordCloud(font_path="jieba_dict/DFT_P7.TTC",
               background_color="white",
               max_words = 2000)
wc.generate(seg_list)

plt.imshow(wc)
plt.axis("off")
plt.show()
