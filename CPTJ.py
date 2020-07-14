#!/usr/bin/env python
# coding: utf-8

# python-中文分词词频统计
# zcmlimi
# ————————————————
# 版权声明：本文为CSDN博主「zcmlimi」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/zcmlimi/java/article/details/90671005
# 
# 20200520

# In[2]:


import os
import csv
import codecs
import jieba
import jieba.posseg as pseg
 
#os.chdir(r'C:\Users\zhuchaoming\Desktop\任务\其他文件\分词')
txt = open("斗破苍穹.txt", encoding="UTF-8").read()

cixingset=1#1 use jieba cixing, 0 don't use it
allL=[5,6,7,8,9,10]#[0] is using jieba 分词, [5,6,7,8,9,10] etc is 全分词
 


# In[3]:


def quanfenciall(txt,allL):
#    allL=range(10) input a str and out ut a list full of continous word in list allL length.
#don't use it for long text since the n is about n**2
    allThe=[]
    for L in allL:
        if L>1:
            allThe=allThe+[txt[a:a+L] for a in range(len(txt)-L)]#+sorted(set(The),key=The.index)
    return allThe

def quanfenci(txt,L):
#    L=10 input a str and out ut a list full of continous word in list allL length.
    allThe=[]
    if L>1:
        allThe=[txt[a:a+L] for a in range(len(txt)-L)]#+sorted(set(The),key=The.index)
    return allThe


# In[4]:


#词xing统计
#stopwords = [line.strip() for line in open("stopword.txt",encoding="gb18030").readlines()]
cixing=[]
if cixingset:
    print('starting jieba cixing')
    cixing = pseg.lcut(txt)#need time


if allL==[0]:
    print('starting jieba cut')
    count  = jieba.lcut_for_search(txt)#need time
else:
    for L in allL:
        print('starting L='+str(L))
        count = quanfenci(txt,L)
        
count=[a for a in count if len(a)>1]#only 2 char or more
allitems={}
for L in allL:
    if L==0:
        print('starting L='+str(L))
        print('starting L='+str(L))

    word_count = {}
    word_flag = {}
    all=[]

#词性统计
    print('dealing jieba cixing')
    for w in cixing:
        word_flag[w.word] = w.flag

    #词频统计
    print('dealing Number')
    for word in count:
        word_count[word] = word_count.get(word, 0) + 1#need time

    #delete less than 5
    for key in list(word_count.keys()):
        if word_count.get(key)<6:
            del word_count[key]
    print('sorting')
    items = list(word_count.items())

    with codecs.open(filename='word_count_L'+str(L)+'.csv', mode='w', encoding='UTF-8')as f:
        write = csv.writer(f, dialect='excel')
        write.writerow(['L='+str(L),'',''])
        write.writerow(["word","count","flag"])


        #按词频排序
        items.sort(key=lambda x: x[1], reverse=True)
        #查询词频字典里关键字的词性
        print('merging')
        for i in range(len(items)):
            word=[]
            word.append(items[i][0])
            word.append(items[i][1])
            # 若词频字典里，该关键字有分辨出词性，则记录，否则为空
            if items[i][0] in word_flag.keys():
                word.append(word_flag[items[i][0]])
            else:
                word.append("")
            all.append(word)


        for res in all:
            write.writerow(res)


# In[15]:


help(cixing[0])


# In[17]:


jupyter notebook --generate-config


# In[36]:


b.append(2)


# In[45]:


b


# In[46]:


b+b


# In[43]:


sorted(set(b),key=b.index)


# In[ ]:




