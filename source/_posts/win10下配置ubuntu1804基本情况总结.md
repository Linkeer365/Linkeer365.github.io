---
title: win10下配置ubuntu1804基本情况总结
tags:
abbrlink: 57668
date: 2020-01-13 00:18:40
---
要做什么:
1. vmware内安装ubuntu1804
2. 设置共享文件夹
3. vmware无界面启动 && xshell进行ssh连接

几点注意:

1. 每次下载大文件or大型软件时, 第一个念头是google搜换源, 第二个念头是硬盘备份(可以方便很多同学...)
2. vmware下载后破解码附带在备份的硬盘内(省得下次再找)
{% asset_img 虚拟机注册码.png 虚拟机注册码 %}
3. 虚拟机安装在ubuntu1804Home下,目录树结构,硬件分配见图
{% asset_img 目录树结构.png 目录树结构 %}
{% asset_img 硬件配置情况.jpg 硬件配置情况 %}
4. 共享文件夹设置的时候虚拟机必须是*关机*状态而不是*挂起*或其他,右键点开"虚拟机设置"
{% asset_img 共享文件夹设置.jpg 共享文件夹设置 %}
5. 可以设置无界面启动的,具体见[这里](`https://web.archive.org/web/20220606030704/https://blog.csdn.net/forest_boy/article/details/49931505`),启动无界面虚拟机代码
`vmrun -T ws start "D:\SubSystem1804\Ubuntu1804\Linkeer365Ubuntu" nogui`
6. linux命令行下ifconfig得到虚拟机的ip地址(没有的话,就先`sudo apt install net-tools`什么的,会有提示的...)
然后xshell直连本机ssh走一波(感谢林煜堃老哥,帮了大忙了这次...)
7. 加入xshell的时候用户名记得要全部小写(不能出现大写字母!否则一直报错:ssh拒绝了密码)

锦上添花:

1. 定制windows的sentTo功能, 使得文件可以直接发到ubuntuWinShare中(xshell负责发送也可以,当然也可以靠listary定制一个目录项...)

2. 把vmrun写到用户环境变量里面, 然后定制.bashrc, 把vmx的path设置为alias, 写一些小函数, Like this:
{% asset_img bashrc关于vmx的函数.jpg bashrc关于vmx的函数 %}

3. 思考一下, 怎样把git bash定制成不输cmd的命令行?  -> 核心问题: `如何使用git bash 进行(托管)系统环境变量的读写呢?`