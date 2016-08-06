#lexicon = ('共同','创造','美好','的','新','世纪')

d = [] # 新建列表存放分词词典读出来的词
with open('E:\自然语言处理\实验2016\分词实验\word_freq_list.utf8','r', encoding='utf-8') as fd:
    flists = fd.readlines()
    for flist in flists:
        #print(flist[11:15])
        s=''
        for i in range(len(flist)):
            if i>11 and flist[i]==' ':
                break
            elif i>10:
                s+=flist[i]
        #print(s)
        d.append(s)
    lexicon = tuple(d) # 将列表转换为元祖
    #print("分词词典：",lexicon)

wordSeg = []    # 新建列表存放切分好的词
maxWordLen = 4  # 最大词长设为4
with open('E:\自然语言处理\实验2016\分词实验\pku_test.utf8','r', encoding='utf-8') as src:
    sentence = src.read()
    sentenceLen = len(sentence)
    wordLen = min(maxWordLen, sentenceLen)
    startPoint = 0
    while startPoint < sentenceLen:  # 从第一个字符循环到最后一个字符
        matched = False    # 假设找不到匹配的词
        for i in range(maxWordLen, 0, -1):  # 从最大词长4递减到1
            string = sentence[startPoint:startPoint+i]  # 取startPoint开始到startPoint+i-1的切片
            if string in lexicon:
                print(string)
                wordSeg.append(string)
                matched = True
                startPoint+=len(string)
                break
        if not matched:    # 假如在词典中找不到匹配
            i = 1
            wordSeg.append(sentence[startPoint])   # 全部切分为单字词
            startPoint += i

with open('E:\自然语言处理\实验2016\分词实验\WordSeg.txt', 'w', encoding='utf-8') as des:
    for word in wordSeg:
        des.write(word+'  ')
