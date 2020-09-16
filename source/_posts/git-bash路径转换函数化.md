---
title: git-bash路径转换函数化
tags:
  - git bash
  - windows-unix路径转换
abbrlink: 39008
date: 2019-08-14 14:13:50
---

- 流程:
    - 文档[Git Bash - Fixing it with alias and Functions](https://coderwall.com/p/_-ypzq/git-bash-fixing-it-with-alias-and-functions)告诉我们可以实现在bashrc下写函数,这些函数可以在git bash下调用
    - 菜鸟教程[shell函数](https://www.runoob.com/linux/linux-shell-func.html)告诉我们怎么写bash函数
    - shell有个只能ret整数的坑[shell-only-ret-ints], 想要ret字符串还是需要利用"$(func params)"外部捕获,参考[shell函数返回字符串](https://blog.csdn.net/zycamym/article/details/45191093)

- 图示
    - {% asset_img w2u转换函数.jpg windows-path to unix-path 转换函数 %}
    - {% asset_img w2u用法示意图.jpg w2u函数用法示意图 %}

- 建议
    - 勤用alias(常用的cd命令什么的建议全部装进去), 真的好用, 我已经用疯了(^_^)

- 感想
    - 人们常说的肉食者鄙, 事实上有一定道理, 我不信一群权威的bash专家, 会没有想到我这个bash小白都能想出来并搞定的问题
    - 香港动乱,历史或将继续增添些许无辜者的鲜血,这种日常一脉相承了上下五千年, 全部被预言中了呀,黑格尔这个糟老头子真是坏得很!
