---
title: github备份hexo博客原始数据
date: 2019-08-04 03:24:12
tags:
    - hexo
    - 自动保存
---

- 缘起:
    - 尽管hexo已交给github pages进行托管, 上传到github却仅仅是编译后的html文件, 不是有效备份
    - 我们要备份博客的md文件, themes文件等等原数据, 以便将来更换电脑时的交接

- 思路:
    1. 所有博客数据分为两类, 一类是原始数据(md文件, 不同用途的_config.yml文件), 一类是编译后的数据(css等等乱七八糟的文件)
        - 原始数据: ![hexo原始数据](/images/hexo原始数据-干净数据.jpg) 
        - 编译后数据: ![hexo垃圾数据](/images/hexo编译数据-脏数据.jpg)
    2. 仅仅关心原始数据的存储安全, 我们也只做原始数据的手动管理, 编译后数据我们不关心
    3. 建立hexo和master两个分支, hexo装着原始数据, master装着编译后的脏数据, 以此区分
    4. git push永远针对原始数据的上载和下载, 于是将hexo作为默认分支

- 过程:
    - hexo分支创建:(如果第一次备份原始数据: 此时你的github应只有一个master分支, 并且master分支像上述那个2019的图一样)
        1. 新建hexo分支, hexo设为默认分支
        2. git clone到Linkeer365Blog文件夹下, 
            - 此时应该是"Blog/Linkeer365.github.io"
            - 因为hexo是默认分支, 所以git clone的就是hexo分支
        3. 把github.io文件夹删除到只剩一个.git
        4. 把原始数据(除了deploy_git以外全部文件)放到github.io文件夹中
            - 要确保"原始数据"这些文件夹里面没有.git文件, 防止git嵌套上传出错
        5. 对github.io文件夹git add, git commit, git push, 检查hexo分支是否一如预期

    - hexo备份数据下载: (如果你是在新电脑上工作: 此时你应该已有hexo分支, 但是新电脑还有配置上的问题)
        1. 完成配置git密钥,nodejs, hexo等等, 估计要再查一遍教程
        2. 新建 Linkeer365Blog, 此时直接git clone, 不需要也不可以hexo init初始化(因为你已经有现成的文件夹和文件了, hexo init会造成_config.yml文件重置)
        3. 在github.io文件夹下, npm install / npm install hexo-deployer-git --save / hexo g -d(最后一个一键生成并部署, 也可以拆开)
        4. 接到上段第5点的种种git操作
    - <del>git commit托管: 一键上传原始数据</del> 老老实实一步步git add; git commit这样来
        - 没有git add会忽略新建的文件的上传!
        - 防止同时编辑的冲突: git pull
            - 看看有没有人正在编辑这个文件
            - 当然一个人就不用啦
        - 全部修改一键上传: git commit -a; git push
        - 全部修改一键上传带注释: git commit -am "2019\8\4\02:38:30"; git push
    - hexo 托管: 一键发博客
        - 发送博客并部署博客: hexo g -d


- 留意点
    - 替身意识: 每次操作文件数据都要先做一个简单备份
    - 每次提交时, 请先进行git commit 操作, 再进行hexo 操作

