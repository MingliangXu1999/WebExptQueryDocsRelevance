# WebExptQueryDocsRelevance

## 给定指定的docs和一系列的querys，给出每个查询的相关度最高的前20个文档id

**utils.py**
- 用于之后的读取test_querys.csv和test_docs.csv，输出为list,并删除list第一个值如query,query_id  
- 在list中删除重复的文章.
- 用于将每一个查询进分词，并将分词的结果输出为list,在更改分词方法是之前，分词方法为jieba.cut_for_search(),更改后为jieba.cut()
分词之后删除停用词

**get_method1.py**:  

第一个算法：使用BM25算法，忽略第三项查询与查询之间的联系，并稍简化，参考 https://cloud.tencent.com/developer/article/1464866.  
其中，get_score函数为处理每个查询与每个文档之间的score,函数内部的average_length_docs=2469通过average_length_docs(docs)函数获得，可能去重之后该值发生变化，尚未修改;  
sort函数返回一个查询与所有最相关文章的前20个结果;  

**get_method2.py:**  
第二个算法： 使用BM25F算法 目前效果最好

**BM25算法结果.txt:**  
列举出每个查询与其相关度最高的20个文章标题，方便查看

**bool加权模型.txt:**  
采用第一个方法之前的第0个方法：bool模型，并进行加权处理，效果不好，已删除源码

**test_querys.txt, test_docs.txt, stopwordsList.txt**  
实验所需文档






