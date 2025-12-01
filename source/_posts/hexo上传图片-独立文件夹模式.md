---
title: hexo上传图片-独立文件夹模式
tags:
abbrlink: 1904
date: 2019-08-13 15:28:10
---
- 问题
    - 前日博客所写的图片上传法, 将图片一股脑儿塞在同一文件夹images下面, 图片一多显然混乱

- 思路
    - 独立文件夹模式: 一个md文件对应一个同名的文件夹, md文件所引用的图片将全部置于该同名文件夹下.

- 条件:
    - 将_config.yml文件(改文件与source文件夹同级)中的post_asset_folder项设为true, 此时执行hexo new filename 就会同时生成filename.md和filename文件夹:[hexo相对路径插入图片](`https://web.archive.org/web/20220605124510/https://yanyinhong.github.io/2017/05/02/How-to-insert-image-in-hexo-post/`)
    - windows下git bash也是可以使用alias进行命令简化的:[win下gitbash的alias教程](`https://web.archive.org/web/20220606030051/https://www.jianshu.com/p/10d013b6e239`)
    - hexo标签插件语法:[% asset_img (这是图片名)风浦可符香.jpg (这是图片描述)可爱的赤木杏 %](`https://web.archive.org/web/20220605124510/https://yanyinhong.github.io/2017/05/02/How-to-insert-image-in-hexo-post/`)

- 流程:
    - 改好config文件并设好alias之后, 我们直接生成现在这个md文件以及对应文件夹.
    - 将图片放进文件夹内
    - 使用标签插件语法, 如下:
        - {% asset_img 风浦可符香.jpg 可爱的赤木杏 %}
        - asset_img不是指文件夹名字, 就叫asset_img, 改动的只有文件名和文件描述.

- 成果:
    - 从当下时间2019年8月13日16:04:45起, 每次写md文件, 图片都会放在对应的同名文件夹下, 便于管理.(之前的图片就不一一更改了)
    - 图片多了一个"comments"的fields我觉得很好, 并且首页和归档都能清晰显示

- 反思
    - 对未来事态的遇见是相当重要的, 不能空凭着好运气.
    - 风浦同学, 一起去摩挲达树海吧, 我对爱对世界这样的词语早就力不从心了! (^_^)


