# -*- coding: utf-8 -*-
# Author: setsal Lan

from gensim.models import doc2vec
from gensim import models
import logging


def main():
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)
    sentences = doc2vec.TaggedLineDocument('output/fb_article_seg.txt')
    model = doc2vec.Doc2Vec( sentences,size=100,window=3 )
    #model.train(sentences)
    model.save('output/doc2vec.model')


if __name__ == "__main__":
	main()
