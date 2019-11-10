#在字符串中找出第一个只出现一次的字符。如输入“abaccdeff”，输出“b”。
#思路：建立一个dict,用于存储字符串中更改字符出现的次数；然后再遍历一次字符串，知道找到第一个字符个数未1的字符输出
def findNotRepeatingChar(str):
    if not str:
        return
    charCounter={}
    for s in str:
        if s not in charCounter:
            charCounter[s]=1
        else:
            charCounter[s]+=1
    for s in str:
        if charCounter[s]==1:
            return s
    return "no such character"

s="abaccdeff"
print(findNotRepeatingChar(s))