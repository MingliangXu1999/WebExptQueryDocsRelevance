import jieba
import readcsv

filepath='./tingyongcibiao.txt'

def fenci(words):
    fencilist=[]
    fencilist=jieba.cut(words)
    return fencilist

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

def delete_stopwords(fencilist):
    stopwords=stopwordslist(filepath)
    outlist=[]
    for word in fencilist:
        if word not in stopwords:
            if word !='\t':
                outlist.append(word)
    return outlist





#print(delete_stopwords(fenci("撒哈拉以南的非洲ppt")))
