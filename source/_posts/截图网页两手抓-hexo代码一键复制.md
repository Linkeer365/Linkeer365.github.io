---
title: 截图网址两手抓-hexo代码一键复制
tags:
  - hexo
  - 上传特定类型文件
abbrlink: 58452
date: 2019-08-14 10:59:44
---
发现知乎的回答许多被删除了,此时纵使拿着网址也无法访问这些资源,可见仅仅保存网址是不安全的,毕竟删除网站的主动权不在我方手中.
知乎有位义士提供了"截图"这个办法[蛏子圣子](https://zhuanlan.zhihu.com/p/31080308),可谓大道至简.
今后任何的博客教程和网站信息, 我都会立刻进行截图保存,做到"截图"和"网址"的两手抓.

- hexo next代码块一键复制教程如下:
    - 感谢小哥[恬雅过客](https://www.jianshu.com/p/3e9d614c1e77)的帮助.
    - 使用fast stone capture进行博文滚动截图, 截图如下: (利用前文中的"标签插件语法")
        - {% asset_img hexo代码块一键复制.jpg hexoNext代码块一键复制功能 %}


- 警示:
    - 每次对"环境文件"进行内部修改的时候,一定要有两个意识
        - 替身意识: 对象文件副本创建与备份
        - 独立化意识: 保存"修改前后"到一个独立文件中, 例如, {修改前(2019年8月14日11:21:07):{...}; 修改代码为{...}.}, 理由是:
            - 防备后患: 替身只能防止当前的出错, 但是有的问题是很久后才会暴露的
            - 便于移植: 其他电脑有相似需求, 可以立刻移植
            - 版本控制: ^举例^ 
                - 做过3次修改, 现在报错是哪一次导致的呢? 我们就可以根据这个独立的文件进行观察&有序进行版本回退.