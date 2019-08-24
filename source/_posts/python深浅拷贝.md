---
title: python深浅拷贝
date: 2019-08-23 12:29:09
tags: 
    - python
    - 深浅拷贝
---
- 缘起
    - 本文是对[python核心编程 Part1](https://www.bilibili.com/video/av39465023)中的深浅拷贝内容的提炼, 非常感激热心的up主

- 背景
    + 众所周知, python默认进行浅拷贝, 而深拷贝需要动用copy模块下的copy.deepcopy
    + 深浅拷贝的实质区别在于是否生成了新的对象, 深拷贝生成了新的对象, 浅拷贝在同一个对象上增加了一个引用
    + 不同对象可以由id进行区分
- 结论
    * deepcopy作用于容器时, 深拷贝是递归进行的
    * copy.copy作用于容器时
        * 容器是可变对象, 此时copy.copy只对第一层进行深拷贝, 其余浅拷贝
        * 容器是不可变对象, 此时copy.copy对容器整体进行浅拷贝

- 演示
```python3
import copy
# l for list

l1,l2=[1,2,3],[1,2,3]
print('l1:{};\tl2:{}'.format(id(l1),id(l2))) 
l12=[l1,l2]

d_l12=copy.deepcopy(l12)

print('l12:{};\td_l12:{}'.format(id(l12),id(d_l12))) # deepcopy外壳实现了深拷贝
print('l1:{};\tl12元素0:{};\td_l12元素0:{}'.format(id(l1),id(l12[0]),id(d_l12[0]))) # deepcopy内部元素同样也实现了深拷贝:l12的元素0就是l1对象本身; 而d_l12元素0不是l1对象
# 由于l2也是同样的情况, 所以就不演示了

# cc for copy_copy obj

cc_l12=copy.copy(l12)

print('l12:{};\tcc_l12:{}'.format(id(l12),id(cc_l12))) # 对l12可变对象: copy.copy外壳实现了深拷贝
print('l1:{};\tl12元素0:{};\tcc_l12元素0:{}'.format(id(l1),id(l12[0]),id(cc_l12[0]))) #  copy.copy内部元素仅仅实现了浅拷贝:l12的元素0就是l1对象本身; 而cc_l12元素0也是l1对象本身

# t for tuple
t12=(l1,l2)
cc_t12=copy.copy(t12)
print('t12:{};\tcc_t12:{}'.format(id(l12),id(cc_l12))) # 对t12可变对象: copy.copy外壳仅实现浅拷贝
print('l1:{};\tt12元素0:{};\tcc_t12元素0:{}'.format(id(l1),id(l12[0]),id(cc_l12[0]))) #  copy.copy内部元素也仅仅实现了浅拷贝:t12的元素0就是l1对象本身; 而cc_t12元素0也是l1对象本身
```
- 图示
    - {% asset_img python深浅拷贝.jpg python深浅拷贝 %}

- 例外事项(2019年8月24日 补充)
    - 昨日学弟问起函数对象为何无法进行深拷贝的问题,以下是代码:
```python3
import copy
def greet():
    print('hw.')
d_greet=copy.deepcopy(greet)
print('greetID:{};\td_greetID:{}'.format(id(greet),id(d_greet))) # 可以看出id是一致的, 说明没有完成深复制
```
    - 能有这样的意识, 其实已经说明该学弟python水平已经非同小可了(甚至想推荐他学一波lambda演算~
    - 然而, 文档的重要性还是要继续重申, 以下文档中搜索"unchanged"就可以查到:[It does “copy” functions and classes (shallow and deeply) by returning the original object](https://docs.python.org/3/library/copy.html)
- 感言
    - 后生可畏, 中年失业什么的还是尽早有准备和觉悟才好.
    - 文档的重要性还是要多重申几次呀, 不要因为库的局限性而浪费了自己的时间, 甚至于怀疑自身的逻辑性什么的真是大可不必.




