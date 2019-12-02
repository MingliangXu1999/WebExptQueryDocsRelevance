
import separatewords as sw
import readcsv
import math


def write_file(filepath,str):
    fh = open(filepath, 'a')
    fh.write(str)
    fh.close()


'''
# BM25F算法(非语义匹配)
## 对于BM25算法的优化
##优化了对文章标题，文章描述的权重分析
'''
def get_score(query,doc,docs,fenci,idf_qi):
    score = 0.0
    title = doc[2]
    content = doc[3]
    #通过对应函数获得平均文章长度
    average_length_docs=2469
    k=0.25+0.75*len(content)/average_length_docs
    Ri=[0 for _ in range(len(fenci))]
    fi=[0 for _ in range(len(fenci))]
    for i in range(len(fenci)):
        start=0
        while(start>=0):
            pos=content.find(fenci[i],start)
            if(pos<0):
                break
            fi[i]=fi[i]+1
            start=pos+len(fenci[i])
    for i in range(len(fenci)):
        Ri[i]=2*fi[i]/(fi[i]+k)
    for i in range (len(fenci)):
        score=score+Ri[i]*idf_qi[i]
    if (title.find(query)==0):
        score = score*2
    if (content.find(query)==0):
        score = score*1.5
    #if(score!=0.0):
    #    print(score)
    return score

def average_length_docs(docs):
    sum=0
    for i in range(len(docs)):
        sum=sum+len(docs[i][3])
    average=sum/len(docs)
    return average

def sort(query,docs):
    scoresdict={}
    fenci = sw.delete_stopwords(sw.fenci(query))
    idf_qi = [0 for _ in range(len(fenci))]
    N=len(docs)
    for i in range(len(fenci)):
        nqi = 0
        for j in range(len(docs)):
            if (fenci[i] in docs[j][3]):
                #print(docs[j][3][1:-1])
                nqi = nqi + 1
        #print("{\"" + fenci[i] + "\" : " + str(nqi) + "},")
        idf_qi[i] = math.log2((N - nqi + 0.5) / (nqi + 0.5))
    for i in range(len(docs)):
        scoresdict.update({i:get_score(query,docs[i],docs,fenci,idf_qi)})
    L=sorted(scoresdict.items(),key=lambda item:item[1])
    return L[-20:]


def querys_docs(querys,docs):
    dictt={}
    write_file('./submission_BM25_更改分词方法_去重.csv','query_id,doc_id'+'\n')
    for i in range(len(querys)):
        print('Completed search: "'+querys[i][0]+'"')
        dictt=sort(querys[i][0], docs)
        for  j in range(20):
            print(querys[i][0]+','+docs[dictt[j][0]][2])
            write_file('./submission_BM25_更改分词方法_去重.csv',str(querys[i][1]+','+docs[dictt[j][0]][0]+'\n'))
        print('\n')



def generateresult():
    path1 = './test_querys.csv'
    path2 = './test_docs.csv'
    querys=readcsv.read_csv(path1)
    docs=readcsv.read_csv(path2)
    querys_docs(querys, docs)

generateresult()