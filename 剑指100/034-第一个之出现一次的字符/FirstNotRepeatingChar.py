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
m="abbaccmdeff"
#print(findNotRepeatingChar(m))




