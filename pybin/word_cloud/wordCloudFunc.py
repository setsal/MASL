from wordcloud import WordCloud


def generateWordCloud(seg_string):
    wc = WordCloud(font_path = "DFT_P7.TTC",
                   background_color = "white", 
                   max_words = 2000)     
    wc.generate(seg_string)
    wc.to_file("output/article.jpg")
    return wc