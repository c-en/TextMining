import re
import math
import sys
import json

def compare_stock(stock_name, year_one, year_two):
    # input AAPL/AAPL10k1A2015.txt, AAPL/AAPL10k1A2016.txt
    in1 = open(stock_name + '/'+ stock_name + '_10K_1A_' + year_one + '.txt', 'r')
    in2 = open(stock_name + '/'+ stock_name + '_10K_1A_' + year_two + '.txt', 'r')

    text1 = in1.read()
    text2 = in2.read()

    # put each text into list of words
    split1 = text1.split(' ')
    split2 = text2.split(' ')

    # toupper each word
    for i in range(len(split1)):
        split1[i] = split1[i].upper()
    for i in range(len(split2)):
        split2[i] = split2[i].upper()

    # create set of words to appear in both texts
    wordSet = set()
    for i in split1:
        wordSet.add(i)
    for i in split2:
        wordSet.add(i)

    # create word vector for each text
    wordCounts1 = {}
    wordCounts2 = {}
    for i in wordSet:
        wordCounts1[i] = 0
        wordCounts2[i] = 0

    for i in split1:
        wordCounts1[i] += 1
    for i in split2:
        wordCounts2[i] += 1

    # find abs distance between word vectors 
    # (this one's pretty bs, don't use for real)
    sumDist = 0
    for i in wordCounts1:
        sumDist += abs(wordCounts1[i] - wordCounts2[i])
    sumDist = 1. - 2. * float(sumDist)/(len(split1) + len(split2))

    # find cosine distance between word vectors
    dot = 0
    for i in wordCounts1:
        dot += wordCounts1[i] * wordCounts2[i]
    norm1 = 0
    for i in wordCounts1:
        norm1 += (wordCounts1[i] ** 2)
    norm2 = 0
    for i in wordCounts2:
        norm2 += (wordCounts2[i] ** 2)
    norm1 = math.sqrt(norm1)
    norm2 = math.sqrt(norm2)
    print(dot)
    print(norm1)
    print(norm2)
    cosDist = dot / (norm1 * norm2
)
    # find jaccard distance between word vectors
    intersect = 0
    union = 0
    for i in wordCounts1:
        intersect += min(wordCounts1[i], wordCounts2[i])
        union += max(wordCounts1[i], wordCounts2[i])
    jaccard = float(intersect) / union

    print(sumDist)
    print(cosDist)
    print(jaccard)

    out_dict = {'sumDist' : sumDist,
                'cosDist' : cosDist,
                'jaccard' : jaccard}

    return out_dict

    #with open(stock_name + '/' + stock_name + '_' + year_two + '.json', 'wb') as f:
    #    json.dump(out_dict, f)


if __name__ == "__main__":
    compare_stock(sys.argv[1], sys.argv[2], sys.argv[3])
