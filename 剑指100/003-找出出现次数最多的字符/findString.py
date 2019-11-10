#coding:utf-8
__author__ = 'admin'
import string
#找出字符串s="aaabbbccceeefff11115555555555"中，字符出现次数最多的字符
#第一种方法，利用字典
s="aaabbbccceeefff111155555555555"
def find_occurenum(s):
    maxnum = 0
    dict={}
    for i in s:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]=dict[i]+1
    #print(dict)
    for j in dict:
        if dict[j]>maxnum:
            maxnum=dict[j]
    return j,maxnum
num,occuretime=find_occurenum(s)
print(num,'出现次数最多，出现了{}次'.format(occuretime))
#第二种方式,使用max方法
s2="aaabbbccceeefff1111555555"
def find_occurenum2(s):
    return max(s,key=s.count)
#print(find_occurenum2(s2))

#第三种方式：先去重，再将去重后的序列作为max,min的参数
def distinct(s3):
    distinct_wordstr=""
    for i in s3:
        if i not in distinct_wordstr:
            distinct_wordstr=distinct_wordstr+i
    return distinct_wordstr
def getmaxchar(wordstr):
    wordstr=wordstr.lower()
    return max(distinct(wordstr),key=wordstr.count)
s3="aaabbbccceeefff111155555555"
print(getmaxchar(s3))


