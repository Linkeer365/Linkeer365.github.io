---
title: windows如何将redis设置为后台运行（注册为服务）
abbrlink: 58592
date: 2020-11-22 22:44:52
tags:
---

[windows 下redis在后台运行](`https://web.archive.org/web/20220606030827/https://blog.csdn.net/yikong2yuxuan/article/details/73195654`)

1. 进入 DOS窗口

2. 在进入Redis的安装目录

3. 输入：`redis-server --service-install redis.windows.conf --loglevel verbose` ( 安装redis服务 )

4.  输入：`redis-server --service-start` ( 启动服务 )

5. 输入：`redis-server --service-stop` （停止服务）

启动指定的配置文件`redis-server --service-start redis.windows-service.conf`
