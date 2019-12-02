import csv

path = './test_querys.csv'

def read_csv(path):
    #读取信息存放在指定列表中
    a=[]
    with open(path,"rt",encoding='utf8') as f:
        csv_read = csv.reader(f)
        for line in csv_read:
            a.append(line)
    a.pop(0)
    return a



