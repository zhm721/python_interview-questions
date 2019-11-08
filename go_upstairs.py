#coding:utf-8
__author__ = 'dmall-zhang'
import sys
sys.setrecursionlimit(100000)
#【Python】Python实现N级台阶，一次可以走1步，2步，3步，一共多少种上楼梯方法
def go_upstairs(num):
    if num == 1:
        return 1
    elif num ==2 :
        return 2
    elif num ==3:
        return 4
    else:
        return go_upstairs(num-1)+go_upstairs(num-2)+go_upstairs(num-3)
#steps=go_upstairs(4)
#print(steps)
#【Python】Python实现N级台阶，一次可以走1步，2步一共多少种上楼梯方法
def go_upstairs2(nums):
    if nums==0:
        return 0
    elif nums==1:
        return 1
    elif nums==2:
        return 2
    else:
        return go_upstairs(nums-1)+go_upstairs2(nums-2)
steps=go_upstairs2(5)
print(steps)



