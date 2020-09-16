---
title: 在windows下使用stack配置基于vscode的简易版Haskell开发环境
tags:
  - IDE配置
  - Haskell
  - vscode
abbrlink: 53092
date: 2019-09-06 16:12:29
---
Haskell的IDE稀少且难以配置,从前天至今日累计花费6小时才成功,以下是配置记录. 

# 参考教程
- (先吐个槽,许多教程漏洞百出, 浪费大家时间, 此处先看我推荐的这些网站, 避免走弯路)
- [蒟蒻中蒟蒻](https://segmentfault.com/a/1190000018257284)
    - 虽是在*nix下的, 但是windows也适用.
    - 这篇文章步骤存在一定问题: 在看完全文前请不要提前操作!
- [hellmonky](https://github.com/hellmonky/note/blob/master/%E8%AF%AD%E8%A8%80%E5%AD%A6%E4%B9%A0%E8%AE%B0%E5%BD%95/%E5%85%B3%E4%BA%8Evscode%E6%90%AD%E5%BB%BAh%E7%8E%AF%E5%A2%83%E7%9A%84%E8%BF%87%E7%A8%8B.md)
    - 这篇文章很不错, 但该篇侧重"Haskell工程项目"的IDE搭建, 与本篇所介绍的"简易版"有所出入.
    - 这篇文章适合"使用Haskell创建大型项目"的用户参考, 再次重申, 本文搭建的是"简易版"开发环境.

# 当前环境
- Windows 10.0.17763

# 核心步骤
- stack安装
- vscode下Haskell插件5个依赖程序安装
- vscode插件路径配置与hs程序调试

# 配置流程
- 参考第一篇[蒟蒻中蒟蒻](https://segmentfault.com/a/1190000018257284)
- 安装stack: 点[这里](https://docs.haskellstack.org/en/stable/install_and_upgrade)进行下载.
    - 我个人希望stack自动更新, 所以我默认安装C盘, 想安装在D盘的朋友请看[这篇文章](https://notes.shinemic.cn/setting-up-haskell-stack-development-environment/)
    - 我个人喜欢自己操作Path环境变量, 所以安装过程中有2个自动Add Path to C:/sc的选项我没有涂黑勾选, 类似下图这样:
    - {% asset_img 环境变量-两个都不选.jpg stack安装过程-两个都不选 %}
- 设置环境变量: Path里头加入stack.exe所在文件夹, 
    - 此处设置环境变量意图为: 为stack install提供便利(即不比麻烦地cd到文件夹下)
    - 其实你们要是会用listary的话, 直接
        - 双击ctrl, 弹出search bar
        - exe:stack, 找到这个stack.exe文件
        - ctrl+shift+D, 复制文件所在文件夹到剪贴板中
        - 在Path中粘贴, 一气呵成.
- 检查cmd下键入stack有没有长长的段落跳出, 有的话执行`stack install`和`stack upgrade`
- 需要跳过的选项:
    - "使用stack创建你的project"这一栏, stack new, stack setup到stack exec my-project-exe统统不需要!
        - 原因: 我们搭建的是"简易版"开发环境, 只需要以下功能:
            - ghci能交互式运行
            - 在智能提示环境下写好单个hs文件后, 能够运行并调试
        - 那个stack new等等是针对一个大型工程的, 我们不需要.
    - 跳过换源
        - 原因: 同上
- 直接来到"搭建vscode"这一栏:
    - 安装插件: Haskell Syntax Highlighting、Haskell ghc-mod 、haskell-linter、Haskelly;共4个
    - 安装插件依赖: ghc-mod、hlint、intero、QuickCheck、stack-run;共5个
        - 先安装ghc-mod, 请直接使用这个命令:
            - `stack install ghc-mod --resolver lts-8.24`
            - 有人会问道stack install后我们已经有lts-14, 请放心, 他们会和平共处的
        - 安装好ghc-mod之后, stack会自动调用ltf-8.24版本, 此时后面的4个插件hlint、intero、QuickCheck、stack-run一定可以一气呵成安装好!
- vscode插件路径配置
    - 新建文件夹HaskellProjects, 加入workplace.
    - File-Preference-settings里面搜索haskell.ghcMod.executablePath和haskell.hlint.executablePath两项
        - 在ghcMod和hlint下分别直接填写ghc-mod和hlint!
- 设置环境变量: Path里头分别加入hlint.exe所在文件夹和ghc-mod.exe文件夹
    - 一般是同一文件夹, 不同就都加一遍
    - 此处设置环境变量意图为: vscode会自动读取环境变量中的hlint和ghc-mod, 也就是haskell.ghcMod.executablePath和haskell.hlint.executablePath两项会被自动补全!
- 在HaskellProjects下新建feibonaqi.hs文件
    - 代码是:
        ```haskell
            module Main (main) where
            fib :: Int -> Int
            fib 0 = 0
            fib 1 = 1
            fib n = fib (n -1) + fib(n - 2)
            main :: IO ()
            main = print $ fib 10
        ``` 
    - 运行, 成功会返回55.
- 过河拆桥, 卸载stack
    - 原因: 
        - 两人幸终: 
            - stack只是一个类似python中的pip程序, 只是一个托管者.在python-pip-vscode三者之间, 显然没有pip不影响python和vscode
            - 基于这样的逻辑, stack可以出局, 只要Haskell和vscode两人幸终即可.
        - stack工具人身份:
            - 依我之见,配置IDE实质:
                - 使用ghc解释(或解释)并运行hs程序.
                - 利用vscode插件, 对Haskell代码的编写提供智能提示.
            - 正因如此, stack仅仅只是用来安装ghc-mod之类的工具人而已
    - 注意事项:
        - 不要把compilers也选了, 不然你的ghc.exe会被误杀!
        - 卸载选项图示:
            - {% asset_img 卸载stack.jpg 注意compilers那项不要选! %}
        - 万一一不小心把compilers也卸载了, 补救办法:
            - 此时插件已经齐了, 只是缺少ghc解释器
            - 直接安装一个Haskell Platform,ghc会随之安装好,其他不用动
            - (需要环境变量就配置一下)

# GHCI安装
- 设置环境变量: Path里头加入ghci.exe所在文件夹
- 顺带一提, winghci配色太outrageous了, 建议命令行下直接操作ghci

# 结论
- 语言可以认为是被不同解释器或编译器所阐释的文本, 核心在解释器--基于这样的意识, 我一开始就知道需要的仅仅是ghc程序.
- 智能提示由插件实现, 插件需要特定依赖--基于这样的意识, 我们借用stack安装好各个插件, 即可实现haskell的智能提示.

# 感想
- "事不过三" 其实可以解读为: "再困难的问题也超不过3天, 因为3天后你不是解决了就是放弃了.(也可以认为你自己被问题解决了~)"所以类似环境配置这种事, 做所有的事都不必心急, 一天不行就第二天再继续看看, 往往都能3天内得到解决, 解决不了的就暂时认输就好了, 不能总是人去解决问题的呀, 老是这样问题岂不是就很没有面子+(^%=%^)+

