def delete_docs(docs):
    i=0
    while(i!=len(docs)-1):
        j=i+1
        while(j!=len(docs)):
            if(docs[i][0]==docs[j][0]):
                #print(i)
                #print(j)
                #print(docs[i])
                #print(docs[j])
                #docs.pop(j)
                del(docs[j])
                j=j-1
            else:
                j=j+1
        i=i+1