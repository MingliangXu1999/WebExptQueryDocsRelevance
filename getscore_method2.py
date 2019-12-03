from utils import *
import math


def write_file(filepath, str):
    fh = open(filepath, 'a')
    fh.write(str)
    fh.close()


'''
# BM25F算法(非语义匹配)
## 对于BM25算法的优化
##优化了对文章标题，文章描述的权重分析
'''

