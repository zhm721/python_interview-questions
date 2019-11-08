#coding:utf-8
__author__ = 'dmall-zhang'
#第一种方法：collections和Counter方法
from collections import Counter
a=(1,5,5,5,5,5,5,2,4,2)
def find_morethanhalfnum(numbers):
    length=len(numbers)
    c=Counter(numbers)#Counter({2: 5, 1: 1, 3: 1, 4: 1, 5: 1})
    dict_c=dict(c)#{1: 1, 2: 5, 3: 1, 4: 1, 5: 1}
    #dict_c.items()#[(1, 1), (2, 5), (3, 1), (4, 1), (5, 1)]
    for k,v in dict_c.items():
        if v>length/2:
            return k
    return 0
#b=find_morethanhalfnum(a)
#print(b)
#第二种方法：使用字典键值对
def find_morethanhalfnum2(numbers):
    dict={}
    for num in numbers:
        if num not in dict:
            dict[num]=1
        else:
            dict[num]+=1
        if dict[num]>len(numbers)/2:
            return num
    return 0
print(find_morethanhalfnum2(a))












