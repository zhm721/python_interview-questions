#coding:utf-8
import datetime
#第一种方式：使用replace方法，复杂度O（N）
def replaceSpace(s):
    str2=s.replace(' ','%20')
    return str2
s=replaceSpace("we are one")
#print(s)
#第二种方式使用join方法
def replaceSpace2(s):
    str2='20%'
    liststr=s.split(' ')#['we', 'are', 'one']
    str3=str2.join(liststr)
    return str3
#print(replaceSpace2("we are one"))
#第三种方式:由于替换字符串之后，字符串长度需要增大。所以可以用第三种方式，
# 先扫描空格个数，计算字符串应有的长度，从后向前一个个字符复制

def replaceSpace3(str):
    #空格计数器
    num_space=0
    for i in str:
        if i==' ':
            num_space=num_space+1
    #新字符串的长度
    new_length=len(str)+2*num_space
    #原始字符串的长度
    index_origin=len(str)-1
    #新字符串的索引
    index_new=new_length-1
    #新的字符数组开辟空间
    new_string=[None for i in range(new_length)]
    #按照顺序往新列表里面放
    while index_origin>=0:
        if str[index_origin]==' ':
            new_string[index_new]='0'
            index_new=index_new-1
            new_string[index_new]='2'
            index_new=index_new-1
            new_string[index_new]='%'
            index_new=index_new-1
        else:
            new_string[index_new]=s[index_origin]
            index_new=index_new-1
        index_origin=index_origin-1
    return ' '.join(new_string)

print(replaceSpace3('we are place'))


