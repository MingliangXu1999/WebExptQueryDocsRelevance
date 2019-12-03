from utils import *
import math
import jieba


'''
# tf-idf算法
'''

def get_score(query, doc, ki, docslength, separateWords, idf_qi):
    score = 0.0
    title = doc[2]
    content = doc[3]
    # 通过对应函数获得平均文章长度
    average_len_docs = 2469
    k = 0.25 + 0.75 * len(content) / average_len_docs
    Tfi = [0 for _ in range(len(separateWords))]
    fi = [0 for _ in range(len(separateWords))]
    for i in range(len(separateWords)):
        start = 0
        while start >= 0:
            pos = content.find(separateWords[i], start)
            if pos < 0:
                break
            fi[i] = fi[i] + 1
            start = pos + len(separateWords[i])
    for i in range(len(separateWords)):
        Tfi[i] = fi[i] / (docslength[ki]+1)
    for i in range(len(separateWords)):
        score = score + Tfi[i] * idf_qi[i]
    if title.find(query) == 0:
        score = score * 2
    if content.find(query) == 0:
        score = score * 1.5
    # if(score!=0.0):
    #    print(score)
    return score


def average_length_docs(docs):
    num = 0
    for i in range(len(docs)):
        num = num + len(docs[i][3])
    average = num / len(docs)
    return average


def sort(query, docs, docslength):
    scorbutic = {}
    separateWords = deleteStopwords(cutWord(query))
    idf_qi = [0 for _ in range(len(separateWords))]
    N = len(docs)
    for i in range(len(separateWords)):
        nqi = 0
        for j in range(len(docs)):
            if separateWords[i] in docs[j][3]:
                # print(docs[j][3][1:-1])
                nqi = nqi + 1
        # print("{\"" + separateWords[i] + "\" : " + str(nqi) + "},")
        idf_qi[i] = math.log2((N) / (nqi + 1))
    for i in range(len(docs)):
        # print(i)
        scorbutic.update({i: get_score(query, docs[i], i, docslength, separateWords, idf_qi)})
    L = sorted(scorbutic.items(), key=lambda item: item[1])
    return L[-20:]


def querys_docs(querys, docs):
    write_file('./submission.csv', 'query_id,doc_id' + '\n')
    docsLength = [len(deleteStopwords(jieba.cut(docInfo[3]))) for docInfo in docs]

    # #####################################################################
    # 此块内容已经读入 '文章长度.txt'中,可以改写代码从文件读入以节约时间
    # for i in range(len(docs)):
    #     docslength.append(len(deleteStopwords(jieba.cut(docs[i][3]))))
        # if(i%100==0):
        #     print(i)
        # print(docslength[i])
    # #####################################################################

    for i in range(len(querys)):
        print('Completed search: "' + querys[i][0] + '"')
        dicta = sort(querys[i][0], docs, docsLength)
        for j in range(20):
            print(querys[i][0] + ',' + docs[dicta[j][0]][2])
            write_file('./submission.csv', str(querys[i][1] + ',' + docs[dicta[j][0]][0] + '\n'))
        print('\n')


def generateResult():
    path1 = './test_querys.csv'
    path2 = './test_docs.csv'
    querys = read_csv(path1)
    docs = read_csv(path2)
    dedupDocs = deduplication(docs)
    querys_docs(querys, dedupDocs)


if __name__=='__main__':
    generateResult()