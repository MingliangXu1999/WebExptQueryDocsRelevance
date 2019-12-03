import csv
import jieba


#######################################
# Read csv file
def read_csv(path):
    # 读取信息存放在指定列表中
    a = []
    with open(path, "rt", encoding='utf8') as f:
        csv_read = csv.reader(f)
        for line in csv_read:
            a.append(line)
    a.pop(0)
    return a


#######################################
# Separate words
stopwordsList_fp = './stopwordsList.txt'

def cutWord(words):
    cutWords = jieba.cut(words)
    return cutWords


def stopwordsList(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


def deleteStopwords(cutWords):
    stopwords = stopwordsList(stopwordsList_fp)
    outlist = []
    for word in cutWords:
        if word not in stopwords and word != '\t':
            outlist.append(word)
    return outlist

#######################################
# Delete repeated docs
def deduplication(docs):
    return list(set([tuple(doc) for doc in docs]))
    # i=0
    # while(i!=len(docs)-1):
    #     j=i+1
    #     while(j!=len(docs)):
    #         if(docs[i][0]==docs[j][0]):
    #             #print(i)
    #             #print(j)
    #             #print(docs[i])
    #             #print(docs[j])
    #             #docs.pop(j)
    #             del(docs[j])
    #             j=j-1
    #         else:
    #             j=j+1
    #     i=i+1