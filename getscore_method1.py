from utils import *
import math


average_length_docs = 2469  # 通过对应函数获得平均文章长度


'''
# BM25算法(非语义匹配)
## 基于分词过后的加权计分算法
    score=\sigma(idf_qi*R(q_i,d))
'''
def get_score(query, doc, queryWords, idf_qi):
    score = 0.0
    title = doc[2]
    content = doc[3]
    qeuryWordsNum = len(queryWords)
    k1 = 1.2    # 经验参数， k1 一般设置为 1.2
    k2 = 500    # 调节因子，一般取值为 0~1000
    b = 0.75    # 调节因子，将 b 设为 0 时，文档长度因素将不起作用，经验表明一般 b=0.75
    K = k1 * ((1 - b) + b * len(content) / average_length_docs)
    fi = [title.count(queryWords[i]) for i in range(qeuryWordsNum)]
    qfi = [query.count(queryWords[i]) for i in range(qeuryWordsNum)]
    R2 = [(1 + k1) * fi[i] / (fi[i] + K) for i in range(qeuryWordsNum)] # 查询词的 term 在 Doc 中的权重
    R3 = [(1 + k2) * qfi[i] / (k2 + qfi[i]) for i in range(qeuryWordsNum)] # 查询词的 term 在查询本身的权重

    for i in range(qeuryWordsNum):
        score += idf_qi[i] * R2[i] * R3[i]
    if (title.find(query) >= 0):
        score = score * 3
    if (content.find(query) >= 0):
        score = score * 1.5
    return score


def sort(query, docs):
    scoresdict={}
    cutQueryWords = deleteStopwords(cutWord(query))
    idf_qi = [0 for _ in range(len(cutQueryWords))]
    N = len(docs)
    for i in range(len(cutQueryWords)):
        df_qi = 0
        for doc in docs:
            if (cutQueryWords[i] in doc[3]):
                df_qi += 1
        idf_qi[i] = math.log10((N + 0.5) / (df_qi + 0.5))
    for i in range(len(docs)):
        scoresdict.update({i:get_score(query, docs[i], cutQueryWords, idf_qi)})
    L=sorted(scoresdict.items(), key=lambda item:item[1])
    return L[-20:]


def querys_docs(querys, docs):
    dictt={}
    write_file('./submission_BM25.csv','query_id,doc_id'+'\n')
    for i in range(len(querys)):
        dictt=sort(querys[i][0], docs)
        for  j in range(20):
            write_file('./submission_BM25.csv',str(querys[i][1]+','+docs[dictt[j][0]][0]+'\n'))
        print('Completed search: "' + querys[i][0] + '"')
        print('Finished percentage: {}%'.format((i + 1) / len(querys) * 100))
        print('\n')


if __name__=='__main__':
    path1 = './test_querys.csv'
    path2 = './test_docs.csv'
    querys = read_csv(path1)
    docs = read_csv(path2)
    dedupDocs = deduplication(docs)
    querys_docs(querys, dedupDocs)