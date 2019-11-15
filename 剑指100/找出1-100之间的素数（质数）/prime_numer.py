#coding:utf-8
#题目：找出1-100之间的质数（素数）
#思路：什么叫做质数？(1)一个大于1的自然数(2)除了1和它自身外，不能被其他自然数整除的数，叫做质数
def find_prime_number():
    prime_list=[]
    #第一步：生成1-100之间的质数,range(1,100),从1开始，range(100),从0开始
    for i in range(1,100):
        #第二步：判断质数是一个大于1的自然数,如果等于1则跳出本次循环
        if i==1:
            continue
        #第二步：找到从2开始到100的质数，除了1和它自身外，不能被其他自然数整数的数，叫质数
        #例如5的质数在（2,3,4）之间找，因为质数是除了1和它本身，所以，就用4除以2和3，因为4可以整除2，所以4不是质数
        for j in range(2,i):
            if i%j==0:
                break
        else:
            prime_list.append(i)
    return prime_list
prime_list2=find_prime_number()
print(prime_list2)





























