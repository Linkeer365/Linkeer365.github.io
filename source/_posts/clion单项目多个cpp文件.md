---
title: clion单项目多个cpp文件设置
date: 2019-08-04 15:20:52
tags:
    - clion
    - cpp
---
- 所需的文档结构是:
    1. 单个CppSnippets项目下, 多个cpp文件, 
    2. 每一个cpp文件中各有一个main函数并保持独立执行
- 条件是:
    1. clion插件, 网址: [clion独立执行单个cpp文件插件](https://plugins.jetbrains.com/plugin/8352-c-c--single-file-execution)
    2. 大项目下, 每个cpp文件不得以main.cpp命名, 由于独立执行,每个cpp文件都必须有main函数
    3. 在每个cpp文件中右键"Add executable for single file", 此时右下角会有弹窗
    4. 查看CMakeLists文件, 多了一行add_executable(filename filename.cpp)即证明build已成功
    5. 左上角下拉框, 选择对应文件运行:![clion左上角下拉框](/images/clion单文件执行样例.jpg)
- 尚未解决的问题:
    - 无法使用中文进行文件命名, 用中文命名则无法reload

