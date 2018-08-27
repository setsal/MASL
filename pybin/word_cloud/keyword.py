import matplotlib.pyplot as plt
import logging
import sys
import io
import os
sys.path.append('../train')
from jiebaFunc import getTestData, getSingleKeywords, init_stopword, getSingleSegment
from wordCloudFunc import generateWordCloud

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

def main():
    logging.basicConfig(format='[%(levelname)s] : %(message)s', level=logging.INFO)

    test_data = getTestData('input/test.txt')

    tags = getSingleKeywords(test_data, 3)

    print("\nkey word: \n")
    print(" ".join(tags))
    print("\n")

    init_stopword()
    seg_list = getSingleSegment(test_data)
    seg_string = " ".join(seg_list)

    wc = generateWordCloud(seg_string)
    """
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    """


if __name__ == "__main__":
	main()
