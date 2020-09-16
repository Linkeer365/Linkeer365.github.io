---
title: python函数装饰器
tags:
  - python
  - 装饰器
abbrlink: 46386
date: 2019-08-23 17:03:58
---
- 缘起
    - 日志与函数计时功能的实现
    - 学弟问起此话题,自己也感到初学时颇费功夫.
- 背景
    - 返回同类指针: 装饰器本质只是函数or类, 唯一不同之处只在于返回值是函数指针or类指针
    - @符号: 装饰器的"@"符号没什么特别, 完全等价于(目标函数定义好后)把目标函数作为实参传进装饰器(再赋值给函数变量)
        - 装饰-赋值: bar=decorator(bar)
        - 调用装饰后函数: bar()
    - "插件"本质: 其他函数与装饰器关系独立, 装饰器执行不依赖也不影响其他函数的功能.
- Demo理解

```python3
# 函数实体的存在是既定的, 不依赖于特定函数名.
import copy

def greet(name):
    return 'Nice to meet you, '+name

print(greet)
# out: <function greet at 0x00000259C5FAD1E0>
## 函数实体已建立, 是<function greet at 0x00000259C5FAD1E0>
## 此时, greet仅仅是一个变量名, 一个函数指针, 它指向的函数对象是<function greet at 0x00000259C5FAD1E0>

sayNiceToMeetYou=greet
# python默认是浅复制, 事实上sayNiceToMeetYou与greet指向同一个对象, 该对象类型是函数

print(id(sayNiceToMeetYou),id(greet))
## out: 1980378239456 1980378239456, 符合假设

del greet

print(sayNiceToMeetYou('lkr')) 
# out: Nice to meet you, lkr, 说明仅仅删除指针, 函数实体并没有被删除

## 正戏开始

def decorator(func):
    def wrapper_who_return_funcPtr():
        # 返回参数列表: https://www.cnblogs.com/snow-backup/p/11077917.html
        # inspect库: https://docs.python.org/3/library/inspect.html
        print('before {} works.'.format(decorator.__code__.co_varnames[0]))
        func()
        print('After {} works.'.format(decorator.__code__.co_varnames[0]))
    return wrapper_who_return_funcPtr

decorator(sayNiceToMeetYou)

# d_sayNiceToMeetYou=copy.deepcopy(sayNiceToMeetYou)
# # print(id(sayNiceToMeetYou),id(d_sayNiceToMeetYou))
## out: 2303771464160 2303771464160, 没有新对象生成, 难道深拷贝也出了问题吗?
## 答案找到了: https://docs.python.org/3.7/library/copy.html 搜索"It does “copy” functions and classes (shallow and deeply), by returning the original object unchanged"

```
- 后记
    - 发现了一篇深度好文[刘志军](https://www.zhihu.com/question/26930016/answer/99243411), 感觉我没什么必要多讲了, 被讲光了(&^%^&)
    - 文章截图:
        - {% asset_img 刘志军-装饰器.jpg 注意functools.wraps的使用可以调取原函数阐释信息 %}




