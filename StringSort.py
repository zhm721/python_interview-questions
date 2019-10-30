#coding:utf-8
"""1、知识点：list1.extend（list2）或者append方法返回的是一个None",是因为两个列表合并后，不会返回一个新的列表
          如果是赋值给其中一个列表就不会返回None了，比如list1=list1.extend(list2)
    2、如果两个列表用‘+’连接会返回一个新的列表,值不会是NONE比如：return list1+list2
    3、append（）方法只能添加一个元素；
        比如：a='1',b=['2','3'] a.append(b)返回的值就是['1',['2','3']];a.extend(b)就返回[1,2,3]
    extend方法更像是一个连接符，一个列表连接另一个列表
"""
#第一种方法
def stringsort(str):
    str1=[]
    str2=[]
    for i in str:
        if  i=='+':
            str1.append(i)
        elif i=='-':
            str2.append(i)
        else:
            return '不是符合的符号'
    str1=str1 + str2
    #return str1+str2
    return str1
str3=stringsort(['-','+','-','+','+','-','-'])
print(str3)

