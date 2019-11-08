__author__ = 'dmall-zhang'
#列表去重并排序
list_str=[10,25,6,-1,5,5,8,7,7]
"""第一种方法，常规方法手写判断"""
#第一步：列表去重
def List_removal(list_str):
    list_str2=[]
    for i in list_str:
        if i not in list_str2:
            list_str2.append(i)
    List_sort(list_str2)
    return list_str2
#第二步列表排序
def List_sort(list_str2):
    for i in range(len(list_str2)-1):
        for j in range(len(list_str2)-1):
            if list_str2[j] >list_str2[j+1]:
                list_str2[j+1],list_str2[j]=list_str2[j],list_str2[j+1]
    return list_str2
#list_str2=List_removal(list_str)
#print(list_str2)

"""第二种方法，使用内置方法：list和set和sorted方法"""
result=sorted(list(set(list_str)))
print(result)

"""使用字典中的fromkeys()方法来去重和排序"""
lst1=[2,1,3,4,1]
lst2=list({}.fromkeys(lst1).keys())
print(lst2)



