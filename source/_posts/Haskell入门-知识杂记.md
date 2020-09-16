---
title: Haskell入门-知识杂记
tags:
  - Haskell
  - 入门向
  - 碎片信息集散
  - 长期更新
abbrlink: 6355
date: 2019-09-06 20:57:50
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
    - [Haskell运算符一览表](https://github.com/Linkeer365/Linkeer365.github.io/tree/hexo/source/_posts/Haskell入门-知识杂记/haskell-operators.pdf)
- 注意事项
    - Haskell没有赋值行为, "-"是唯一的一元运算符, 表示"将减号作用于operand"
    - 能写括号就不要懒, 不多提

## (2019年9月6日23:00:45) 待解决问题:
- <del>Haskell运算符的{结合律}{优先级}{函数功能}, 有没有一个专门的cheatSheet能写清楚的?</del>
    - 解决办法1:
        - ghci键入`:info operator_name`或`:i operator_name`, 最下面infixl或者infixr, 带一个优先级数字
            - infixl or infixr 表示"左结合"或者"右结合"
            - infix后面的数字优先级: 9>8>7>6...>1
    - 解决办法2:
        - 概括:[Haskell-98Report-exps](https://www.haskell.org/onlinereport/exps.html)
        - 查表:[Haskell-98Report-infixity](https://www.haskell.org/onlinereport/decls.html#fixity)


## (2019年9月6日23:04:35) 待整理资料:
- 除却运算符一览表, 目前还收集到两份CheatSheets:
    - [UCS-cheatSheet](https://github.com/Linkeer365/Linkeer365.github.io/tree/hexo/source/_posts/Haskell入门-知识杂记/haskell-ucs-CheatSheet.pdf)
    - [Hackage-cheatSheet](https://github.com/Linkeer365/Linkeer365.github.io/tree/hexo/source/_posts/Haskell入门-知识杂记/HaskellHackageCheatSheet.pdf)

## (2019年9月7日13:42:33) 找到"ghci缩写命令" 表:
- 原网页:[ghc-commands](https://github.com/ghc/ghc/blob/e3ec2e7ae94524ebd111963faf34b84d942265b4/ghc/GHCi/UI.hs#L160)
- 用法指导:[so :c means :cd, :d means :def, follow the order.](https://stackoverflow.com/questions/47265489/is-there-a-list-of-ghci-abbreviated-commands)
- 缩写命令表:[这里](https://github.com/Linkeer365/Linkeer365.github.io/tree/hexo/source/_posts/Haskell入门-知识杂记\ghci-abbreviated-commands.pdf)

## 定义变量
- 阶级性: 
    - 内容: 函数, 变量必须用小写字母开头; 类型必须用大写字母开头.
    - 好处: 便于分辨函数与类型.
- 在ghci中let定义临时变量:
    - ghci> `let e = exp 1`
    - 注意let用法在ghci和haskell script存在不同, 尽量不要用let定义
    - <del>(2019年9月7日15:20:27) 待补充: 常规形式的变量定义是?</del>
        - 就是`x=5`这种

## (2019年9月11日19:39:32) Haskell参考资料已汇总
- 此后只需记录一些不很重要的细节即可
- {% asset_img Haskell-浏览器书签.jpg Haskell部分书签 %}

## ASCII字符码
- 举例, '\100' 表示ASCII=100的那个字符, 即: '\100' -> 'd'
    ` ghci>:t '\100'`
    ` '\100' :: Char`
- '\'转义功能和其他语言一致, 所以:
    ` ghci> putStrLn '\\'`
    ` \`

## (2019年9月11日19:57:54) Haskell风格补充
- 注意, Haskell风格除了"类型大写, 函数与变量小写"之外, 还有"尽可能采用驼峰命名"这一条

## What is 'xs'?
- You might wonder where the variable name xs comes from in the Haskell function. This is a common naming pattern for lists: you can read the s as a suffix, so the name is essentially “plural of x”. 10 comments
- [这里](http://book.realworldhaskell.org/read/types-and-functions.html#x_iB1)

## Type variable -> Good naming.
- 小写开头就行了: Type variables can have any names with lowercase alphas.
- 例子:
```haskell
f :: Num num => num -> num
f x  = 4*x+1

main :: IO()
main = print $ f 5
```


