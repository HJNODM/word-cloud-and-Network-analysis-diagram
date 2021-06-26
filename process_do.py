#!/usr/bin/env python
#   -*-   coding:   cp936   -*-  使用中文
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']   #设置字体为SimHei显示中文
plt.rcParams['axes.unicode_minus']=False     #设置正常显示字符
#设置线条样式  plt.rcParams['lines.linestyle'] = '-.'
#设置线条宽度 plt.rcParams['lines.linewidth'] = 3

df = pd.read_excel('comments_2.xlsx')
url = list(df['url'])
comments = list(df['remove_text_tags'])
info = {}
for i in range(len(url)):
    if url[i] in info:
        info[url[i]] += 1
    else:
        info[url[i]] = 1
df = pd.DataFrame(info, index=[0])
df = df.T
df.columns = ['sum']
df = df[df['sum'] >= 100]
target = list(df.index)
df = pd.read_excel('前100部图书信息表.xlsx')
book_name = list(df['bookname'])
url_list = list(df['url'])

target_name = []
target_comment = []
info = {}
for i in range(len(target)):
    for j in range(len(url_list)):
        if (target[i] == url_list[j]):
            target_name.append(book_name[j])
            info[book_name[j]] = None
            break
print(info)
for i in range(len(target)):
    for j in range(len(url)):
        if (target[i] == url[j]):
            if info[target_name[i]] == None:
                info[target_name[i]] = comments[j].split(' ')
            else:
                info[target_name[i]].extend(comments[j].split(' '))

for i in info:
    while '' in info[i]:
        info[i].remove('')

num_data = []
for it in info:
    temp_data = []
    for itt in info:
        if info[it] == info[itt]:
            temp_data.append(len(info[it]))
        else:
            sum = 0
            for i in range(576):
                if info[itt][i] in info[it]:
                    sum += 1
            temp_data.append(sum)
    num_data.append(temp_data)

df = pd.DataFrame(num_data)
df.columns = target_name
df.index = target_name
# print(df)

plt.figure(figsize=(16, 10))
ng = nx.Graph()
nf2 = nx.from_pandas_adjacency(df)
nx.draw(nf2, with_labels=True, node_color='yellow')
plt.show()
