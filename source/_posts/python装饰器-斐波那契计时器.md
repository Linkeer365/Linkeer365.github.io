---
title: python装饰器_斐波那契计时器
tags:
abbrlink: 31338
date: 2019-08-24 23:31:54
---
装饰器的实例1-代码计时器,说明都写在代码注释中了~
```python3
import time

def timer(func):
    def wrapper(*arguments,**keyword_arguments): # 参数有无与多少不确定, 关键字参数有无与多少不确定
        start=time.time()
        ret=func(*arguments,**keyword_arguments) # 与前文类似, 参数有无与多少不确定
        end=time.time()
        print('FuncName:{};\nResult:{}\nTime Spent:\t{}s'.format(getattr(func,'__name__'),ret,end-start),file=open('D:\跑速情况.txt','a'))
        # 可以先dir(func) 查出func有__name__这个attr, 于是用函数getattr(funcName, funcAttrName)
        return ret # 很关键, 因为func有返回值所以要写ret(其实没有返回值也写一下没什么问题)
    return wrapper # 装饰器本质: ret内层函数

# 注意: 带参数的装饰器指的是装饰器有参数, 就是最外层的timer(func,args),
## 被装饰函数有参数, 直接在内部处理就可以, ret=func(*arguments,**keyword_arguments)

@timer
def m1_feibonaqi(n,visited=[]): # 改进版递归型斐波那契, 区分于远坂sb无脑递归型在于加入visited使得不用重复计算
    if n==1 or n==2:
        return 1
    else:
        if bool(visited)==0:
            ori_visited=[1,1].extend([None for each in range(3,n+1)])
            visited=ori_visited
        else:
            if visited[n-2]==None:
                tail=m1_feibonaqi(n-2)
                visited[n-2]=tail
            if visited[n-1]==None:
                head=m1_feibonaqi(n-1)
                visited[n-1]=head
            return visited[n-1]+visited[n-2]
        return m1_feibonaqi(n-1)+m1_feibonaqi(n-2)

@timer
def m1_feibonaqi(n): # sb无脑递归型, 可以拿来测下栈帧深度
    if n==1 or n==2:
        return 1
    else:
        return m1_feibonaqi(n-1)+m1_feibonaqi(n-2)

@timer
def m2_feibonaqi(n): # 正常型斐波那契
    if n==1 or n==2:
        return 1
    else:
        f1,f2=1,1
        head,tail=f2,f1
        cnt=2
        while cnt<n:
            cnt+=1
            next_val=head+tail
            head,tail=next_val,head
        return next_val

@timer
def m3_feibonaqi(n,visited=[]): # 改进版递归型斐波那契, 区分于远坂sb无脑递归型在于加入visited使得不用重复计算
    if n==1 or n==2:
        return 1
    else:
        if bool(visited)==0:
            ori_visited=[1,1].extend([None for each in range(3,n+1)])
            visited=ori_visited
        else:
            if visited[n-2]==None:
                tail=m1_feibonaqi(n-2,visited)
                visited[n-2]=tail
            if visited[n-1]==None:
                head=m1_feibonaqi(n-1,visited)
                visited[n-1]=head
            return visited[n-1]+visited[n-2]
        return m3_feibonaqi(n-1,visited)+m3_feibonaqi(n-2,visited)


m1_feibonaqi(10) # 这个只能跑20以内的
print('----分界线12----',file=open('D:\跑速情况.txt','a'))
m2_feibonaqi(10**5) # 这个可以跑10万以内的
print('----分界线23----',file=open('D:\跑速情况.txt','a'))
m3_feibonaqi(10) # 这个也同样只能跑20以内的

## 实际上m1和m3跑出来结果是一样的(^7$7^), 难受~
```
希望大家能够更清楚地了解装饰器的实质与用法, 以后依据不同的需求我估计还会写一些其他的~