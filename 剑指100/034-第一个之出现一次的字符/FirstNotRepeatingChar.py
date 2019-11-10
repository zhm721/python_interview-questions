#在字符串中找出第一个只出现一次的字符。如输入“amamccdeff”，输出“b”。
#思路：建立一个dict,用于存储字符串中更改字符出现的次数；然后再遍历一次字符串，知道找到第一个字符个数为1的字符输出
#第一种方法
def findNotRepeatingChar(str):
    a=[]
    if not str:
        return
    charCounter={}
    for s in str:
        if s not in charCounter:
            charCounter[s]=1
        else:
            charCounter[s]+=1
    #注释掉的一段是返回所有出现一次的字符
    # for char in charCounter:
    #     if charCounter[char]==1:
    #         a.append(char)
    #return a
    for s in str:
        if charCounter[s]==1:
            return s
    return "no such character"
m="anbbaccmdeff"
#print(findNotRepeatingChar(m))
#第二种方法:直接用遍历的方式
def findNotRepeatingChar2(str):
    if not str:
        return -1
    else:
        for i in str:
            if str.count(i)==1:
                #return str.index(i)#返回第一次出现一次的字符的位置
                return i #直接返回这个字符
print(findNotRepeatingChar2(m))





