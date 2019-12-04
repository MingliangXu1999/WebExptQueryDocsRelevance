from utils import *
import math

AVL_CONTENT = 2469  # 通过对应函数获得平均文章长度
AVL_TITLE = 28

'''
# BM25F算法(非语义匹配)
## 对于BM25算法的优化
##优化了对文章标题，文章描述的权重分析
'''
def get_score_BM25F(query, doc, queryWords, idf_qi):
    score = 0.0
    title = doc[2]
    content = doc[3]
    qeuryWordsNum = len(queryWords)

    boost_t = 10
    boost_c = 1
    b_t = 0.75
    b_c = 0.75
    k1 = 1.2  # 经验参数， k1 一般设置为 1.2

    weight_td = [0 for _ in range(qeuryWordsNum)]
    for i in range(qeuryWordsNum):
        weight_td[i] += (title.count(queryWords[i]) * boost_t) / ((1 - b_t) + b_t * len(title)/AVL_TITLE)
        weight_td[i] += (content.count(queryWords[i]) * boost_c) / ((1 - b_c) + b_c * len(content)/AVL_CONTENT)
    for i in range(qeuryWordsNum):
        score += idf_qi[i] * weight_td[i] / (k1 + weight_td[i])

    return score


def sort(query, docs):
    scoresdict={}
    cutQueryWords = deleteStopwords(cutWord(query))
    idf_t = [0 for _ in range(len(cutQueryWords))]
    N = len(docs)
    for i in range(len(cutQueryWords)):
        ni = 0
        for doc in docs:
            if (cutQueryWords[i] in doc[3]):
                ni += 1
        idf_t[i] = math.log10((N + 0.5) / (ni + 0.5))
    for i in range(len(docs)):
        scoresdict.update({i : get_score_BM25F(query, docs[i], cutQueryWords, idf_t)})
    L=sorted(scoresdict.items(), key=lambda item:item[1])
    return L[-20:]


def querys_docs(querys, docs):
    dictt={}
    write_file('./submission_BM25F.csv','query_id,doc_id'+'\n')
    for i in range(len(querys)):
        dictt=sort(querys[i][0], docs)
        for  j in range(20):
            write_file('./submission_BM25F.csv',str(querys[i][1]+','+docs[dictt[j][0]][0]+'\n'))
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