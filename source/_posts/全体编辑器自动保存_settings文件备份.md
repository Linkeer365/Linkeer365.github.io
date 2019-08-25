---
title: 全体编辑器自动保存 & settings文件收集整理
tags:
    - 自动保存
---

缘起:
- 听说有人资料遗失痛不欲生, 罪魁祸首是忘记保存, 因此, 所有涉及到原创的资料都要设置自动保存.
- 如果电脑崩溃, 资料尽管已经保存好, 然而纷繁的设置却同样令人头疼, 因此settings文件也要定期导出并备份.

思路:
- "自动保存"是settings的一种, 所以实质是解决settings保存问题.
- 设置自动保存后, "此项设置"往往也在settings文件夹内, 故要先设置自动保存, 再设置settings文件备份
- settings文件往往不大, 故可以用其中一个repo来存储它

流程:

- 通过manictime, 得到这些天来动用过哪些编辑器
    - cent浏览器(no)
    - Adobe Reader, 福昕阅读器(no)
    - Jetbrains三兄贵, pycharm, Clion, Idea(yes)
    - vscode(yes)
    - notepad++(no)
    - 搜狗输入法(云端, 不需要)
    - Office三件套,ppt, excel, word(太少,不需要)
    - listary日常搞姬(yes)
    - nomeiryo 字体修改(yes)
- 对这些编辑器设置自动保存
    - cent浏览器
        - 记得登录谷歌, 实现书签与插件的自动保存
        - 好像不支持settings导出emmm
    - Adobe Reader, 福昕阅读器
        - 好像不支持settings的导出?
    - Jetbrains三兄贵
        - 自动保存: 
            - Settings >> Apperance & Behavior >> System Settings >> Save files on frame deactivation automatically(180sec)
        - 导出设置:
            - 自动保存完后请先关闭再打开
            -  File >> Export settings
    - vscode
        - 自动保存:
            - File >> Preferences >> settings >> 搜索"Autosave" >> afterdelay >> 180000ms
        - 导出设置:
            - 随便找一个.vscode文件, 复制settings.json和tasks.json并压缩即可
    - office三件套:
        - 自动保存:
            - 文件-选项-保存-1分钟
        - 导出设置: 选项太少, 可以忽略
    - notepad++
        - 自动保存:
            - 重装32bit版本, 安装[plugins manager](https://github.com/bruderstein/nppPluginManager/releases), 新建把plugins文件夹内的pluginManager放在安装目录plugins下面
            - plugin Manager下找autosave插件, 随后进行设置
        - 导出设置:
            - 只进行插件的备份?
    - listary
        - 导出设置: Roaming下userdata
    - 字体Nomeiryo
        - 直接保存字体即可

- 导出这些编辑器的设置, 并每月设置提醒更新这些设置
- 统合settings文件, 上传百度云盘(github太小放不下)



