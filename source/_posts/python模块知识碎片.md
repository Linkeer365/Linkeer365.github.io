---
title: python模块知识碎片
tags:
abbrlink: 27979
date: 2019-08-23 13:19:05
---
- 缘起
    - 本文是对[python核心编程 Part1](`https://web.archive.org/web/20220605125652/https://www.bilibili.com/video/av39465023`)中的深浅拷贝内容的提炼, 非常感激热心的up主
- 结论
    - import搜索目录为sys.path这个列表
        - 由于是列表所以可以更改, 比如加入github.io文件夹什么的
        - sys.path的改变不跨文件, 可以拿两个py文件自己试下
    - 使用M模块中途M模块被修改, 使用imp.reload(module)进行模块的重新导入
        - 质疑: 是否本就不应该在使用某个模块的中途去修改这个模块
        - 全模块导入时存在模块依赖: 如果M模块自身也import了其他模块M1,M2, 那么这些M1,M2并不会被导入: 详见[python全模块reload的坑](`https://web.archive.org/web/20220605145743/https://blog.csdn.net/dashoumeixi/article/details/80819059`)
    - 避免循环引用
        - 循环引用: 存在a.py与b.py, 此时a.py中写import b同时b.py中写import a
        - 设计观点: "类-接口"模式的重要性, 包括:
            - 类C1,C2,C3...不互相import对方
            - import工作完全由接口实现, 接口I1,I2也要做到相对独立
            - {%asset_img python接口与类分离设计.jpg 设计思想: 接口与类分离实现 %}
