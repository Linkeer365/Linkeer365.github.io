---
title: git bash下windows-style路径转换
date: 2019-08-14 11:50:40
tags: 
    - git-bash
    - windows-unix路径转换
---
- 缘起:
    - 在windows平台下,由教程[善用佳软winr](https://xbeta.info/win-run.htm), 我们知道可以利用winr唤醒gitbash(我记为gb), 但是进入gitbash后当前目录往往并不是工作目录, 需要cd几轮进行跳转,这件事很烦人.

- 思路
    - 由listary的"路径复制"功能, 可以迅速获得某个文件的地址(或者其所在文件夹) 举例:
        - {% asset_img listary复制路径至剪贴板.jpg listary复制路径至剪贴板-如图红色框框 %}
        - 这个路径显然是windows-style的路径, 但是我们需要的是unix like的路径才能直接在git bash里面cd {some unix-like path}这样子
    - 既然我们可以轻松地复制得到一个 windows-like的路径, 类似这样:{D:\备份地点\文档资料备份地点\cmBooks\Cpp\风浦可符香.jpg}, 那么有没有一个path conversion, 能够接受windows-path, 然后返回Unix-path的呢?
    - 倘若有,windows-path我们先convert成为unix-path, 然后直接把unix-path传给cd就可以了

- 资料 & 分析
    - stackOverflow上找到[Windows PATH to posix path conversion in bash](https://stackoverflow.com/questions/13701218/windows-path-to-posix-path-conversion-in-bash)
    - csdn上找到[shell命令结果赋值给变量](https://blog.csdn.net/zwt0909/article/details/52813388)
    - 很明显, 只要用wp(windows-path)和up(unix-path)两个变量即可达成.

- 举例分析
    - 要访问这个文件夹:{D:\备份地点\文档资料备份地点\cmBooks\Cpp}
    - 首先listary获取路径(过于简单,省略), 此时路径已经在我们的剪贴板中了
    - git bash下
        - wp='D:\备份地点\文档资料备份地点\cmBooks\Cpp'
        - up=$(echo "/$wp" | sed -e 's/\\/\//g' -e 's/://')
            - 注意这个$wp前面的backslash不能省略!
        - cd $up, 大功告成
    - 一图胜千言:
        - {% asset_img 路径转换示意图.jpg wp是windows-path; up是unix-path %}

- 反思
    - 能不能利用alias或者自定义函数对这个进行直接调用呢?

- 感想
    - 很久以前我在github的git-for-windows下面问了一圈,没人鸟我,这个如此简单的痛点竟然没人解决,妈的.
    - 每天我都要一遍遍告诉自己不是一个天才, 真累啊~

- 参考信息截图(不po了, 就是一个记录而已)已存储