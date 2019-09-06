---
title: Haskell入门-知识杂记
date: 2019-09-06 20:57:50
tags:
    - Haskell
    - 入门向
    - 碎片信息集散
    - 长期更新
---
初窥门径, 长期更新

## GHC
- GHC=ghc(编译器)+ghci(i=interactive, 交互式)+runghc(解释器, 不需要编译)

## ghci
- i=interactive, 交互式
- 类似于python的IDLE, 同时也都有调试功能.
- 交互式Shell都有调试功能吗?

### Prelude
- Prelude是一个常用模块, 这里`Prelude>` 表示预加载了Prelude模块
- 加载其他模块:
    - 指令: `:module 模块名{例如, Data.Ratio}`或者`:m 模块名{例如, Data.Ratio}`
    - prompt增长: `Prelude>` -> `Prelude Data.Ratio>`
- Prelude提示符的替代:
    - 指令: `:set prompt "ghci>"`
    - 可以乱写: `:set prompt "sangaizhonggai>"`
    - 静态效果: 改完后导入模块不显示导入名.
    - 重置指令: `:unset prompt`
- 建议:
    - prompt增长起到了提示功能, 我认为有利
    - (除非左边太长)不建议瞎改成其他名字, 没什么意义

### ghci运算符
- Haskell除法默认不floor, 不截断
    - 例子: 7/2=3.5
- 数学上,二元运算符(binary operator)可摆放在运算数(operand)的不同位置, 分成3类:
    - 前缀运算符, 中缀运算符, 后缀运算符(自然对应3种表达式, 不多提)
    - 这些"缀"只适用于二元运算符, 其他{1元}或{3元及以上}都不行
- Haskell不支持后缀表达式, 比如`5!`这种就没有.
- Haskell下前中缀转换:
    - 前缀(prefix)转中缀(infix): 用"`"包起来
    - 中缀(infix)转前缀(prefix): 用小括号包起来
- Hasekll不等号是"/="(正斜杠+等号)而不是"!="
    - (想起之前有人问什么是正反斜杠: 斜率k>0是正斜杠, k<0是反斜杠^_^)
- Haskell运算符一览表
    - 初中数学老师: "表的好处有啥子呦↘一目↗了然↘一遍↗就记住~忘了↗就查↘"
    - {% pdf  https://github.com/Linkeer365/Linkeer365.github.io/tree/hexo/source/_posts/Haskell入门-知识杂记/haskell-operators.pdf haskell-operators一览表%}
- 注意事项
    - Haskell没有赋值行为, "-"是唯一的一元运算符, 表示"将减号作用于operand"
    - 能写括号就不要懒, 不多提

## (2019年9月6日23:00:45) 待解决问题:
    - Haskell运算符的{结合律}{优先级}{函数功能}, 有没有一个专门的cheatSheet能写清楚的?

## (2019年9月6日23:04:35) 待整理资料:
- 除却运算符一览表, 目前还收集到两份CheatSheets:
    - {%pdf https://github.com/Linkeer365/Linkeer365.github.io/tree/hexo/source/_posts/Haskell入门-知识杂记/haskell-ucs-CheatSheet.pdf  haskell-ucs-CheatSheet %}
    - {%pdf https://github.com/Linkeer365/Linkeer365.github.io/tree/hexo/source/_posts/Haskell入门-知识杂记/HaskellHackageCheatSheet.pdf HaskellHackageCheatSheet %}





