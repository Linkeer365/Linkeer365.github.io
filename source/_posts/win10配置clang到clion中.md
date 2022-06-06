---
title: win10配置clang到clion中
tags:
  - clion
  - clang配置
  - win10
abbrlink: 38389
date: 2019-10-22 19:48:33
---
考虑到主页[千里冰封](`https://web.archive.org/web/20220605130206/https://www.zhihu.com/question/351744551/answer/865665382`)的推荐, 我去安装了试试, 以下是简要记录(我的运气还是挺好的, 至少没有看到一些劝退的帖子, 安装过程算是非常顺利的一次了...)
1. 根据[这里](`https://web.archive.org/web/20210618170309/https://intellij-support.jetbrains.com/hc/en-us/community/posts/206606735-Using-Clang-With-CLion-on-Windows?page=1`#community_comment_115000631284)我们知道一共有3件事要做, {安装mingw64和msys2}-{在msys2中安装llvm和clang}-{在clion中配置cmake和toolchain选项}
2. 安装mingw64和msys2不用提了...
3. 在msys2中安装llvm和clang,命令是`pacman -S mingw-w64-x86_64-llvm`和`pacman -S mingw-w64-x86_64-clang`(注意有先后)都懂得, 只要一涉及这种命令行下载东西的时候, 就立马先到网上查一下"换源"什么的, 于是搜索"msys2 换源", 然后在[这里](`https://web.archive.org/web/20220605130408/https://mirror.tuna.tsinghua.edu.cn/help/msys2/`)找到了答案, 这就是一种意识, 很多时候应该变成一种条件反射的东西, 哦一旦出现命令行下载东西就立马换源换源...如果不是命令行的话呢, 就请买一个IDM, 你会发现你后半生的下载会非常自在的...
4. clion中的配置过程, 首先按照[原网页](`https://web.archive.org/web/20210618170309/https://intellij-support.jetbrains.com/hc/en-us/community/posts/206606735-Using-Clang-With-CLion-on-Windows?page=1`#community_comment_115000631284)上面显示的配置cmake选项的确是OK的, 那个CC={sth1}, CXX={sth2}一看就知道是环境变量里面的键值对, 所以直接将CC和CXX配置到环境变量里头去即可, 但并没有结束, 此处没有考虑到toolchain的情况, 下面是toolchain的配置.
5. 根据[这里](`https://web.archive.org/web/20210512030509/https://intellij-support.jetbrains.com/hc/en-us/community/posts/360000394670-How-can-I-configure-LLVM-Clang-6-0-with-CLION-2018-1`)我们找到这段话`You can't use clang in CLion on Windows without having MinGW or Cygwin installed. You can try the following:`, 说明我们还是要把mingw放在Environment下, 只是make的工具全部换成clang系列的即可 (还有就是能让clion自己detect就不必手动加入绝对路径了...), 这里不多废话, 一图胜千言
6. 第5步图
- {% asset_img clion_clang配置_toolchain_mingw部分.jpg clion_clang配置_toolchain_mingw部分 %}
- {% asset_img clion_clang配置_toolchain_clang部分.jpg clion_clang配置_toolchain_mingw部分 %}
7. 成果是这样的
- {% asset_img clang报错信息.jpg clang报错信息 %}
- 下次试着把cl.exe也安装上去, 看看每家编译器的水准如何hh~

