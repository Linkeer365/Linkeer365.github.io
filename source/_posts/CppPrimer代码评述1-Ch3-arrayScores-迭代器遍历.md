---
title: CppPrimer代码评述1-Ch3_arrayScores-迭代器遍历
tags:
  - cpp
  - CppPrimer读书笔记
  - 迭代器
  - 代码评述系列
abbrlink: 4744
date: 2019-09-16 20:51:01
---
新坑是代码评述系列, 评述写在注释里, 非常主观非常粗俗, 但可能可以给我带来一点安慰, 感觉自己好勤奋的样子.

## 碎碎念1-C++迭代器到底要实现什么?好在哪里?
这边先简单提一下C++的迭代器, 我们知道C++一共有5种(甚至更多?)种迭代器, 具体请看[这里](`https://web.archive.org/web/20220605114953/https://blog.csdn.net/sim_szm/article/details/8980879`), 但是归根结底, 在实现"遍历"这个事情上, 我们需要的迭代器只要能够实现这两点就足够贴心了:
1. 通用接口: 
    - 对所有容器类与"类似容器类的类型"(比如String类型), 提供相似的接口(目前的实现, 就是T.begin(), T.end()两个成员函数)
    - 对原生数组提供与容器类尽可能相似的操作.
2. 防越界: 
    - 利用边界条件实现"迭代终止"的判断, 而不是依靠程序员自己判断
目前存在的问题是, 因为数组显然不是类型类, 所以不可能有T.begin(), T.end()这样的成员函数, 但是我们还是希望实现一个通用接口, 于是我们使用`<iterator>`里面的cbegin和cend两个成员函数, 他们接受数组并返回头尾指针(并且由于加c所以还是个常量, 省的以后多事), 如此一来, 我们就能够实现: 完完全全使用"迭代器"(或类似迭代器的"迭代指针常量")进行遍历这一宏伟目标了, 我觉得有点像"百代皆从秦制"那种美感, 具体请看[这里](`https://web.archive.org/web/20210315030549/https://blog.csdn.net/qq_37653144/article/details/78552479`)

## 碎碎念2-符号记法中的一些玄机
这边再扯一点关于一些符号记法的东西, 首先我们知道每一种语言它的记号都是有一定区别的, 但是在这些区别中也是有通用的记法(或者干脆叫做"创造者们的一种默契"好了^_^), 这些通用的记法比如说都使用`[]`作为数组索引的算子; 不同的东西我们可以认为是某种特定的"Style风格", 比如同样是定义普通数组, C/C++喜欢中置括号(C sytle), 而Java喜欢把括号提前(Java style), 这里面也大有玄机: 
我猜测, 因为我们知道Java不像C++, 天天要拖着C这个弟弟然后无限纵容(兼容), 所以很快就走向了"容器"+"切面"这样的编程模式了(这也是为什么后面会形成那么多的编程范式的原因之一), 也就是"容器"这个更抽象的概念与思想很可能是Java先广泛运用的, 比如 `Int[]`, 很可能就体现出来一个"容器"的雏形, 因为这种写法就意味着`Int[]`与`Int`两个概念的分离, {"整型指针", "整型数组"}是容器一类, {"整型"}是元素一类, 他们之间概念的差异被Java发扬出来, 这是一个体现.
我猜测,为什么C语言一开始定义数组使用中置括号, 可能与"内存操作"的印象有关, 因为本身"数组"的应用天生就与"遍历"分不开(sizeof我们都知道是"编译期决定"的, 所以也不能帮忙对数组长短进行控制), 然而从内存视角而言Int数组和Int差别其实不是很大(他们的指针都只能指向一个块块), 因此他们认为Int Array就是Int, 只是需要对后面的若干块进行管理, 这种想法很自然就不会将`[]`剃刀变量前面, 因为以这种内存观点来看, `[]`提前反而是一种误解了, 认为这个指针指向另一个数组指针了.

## 碎碎念3-关于逗号与分号的使用分析
代码后半部分注释进行了探讨, 在此不做过多说明.

## 代码评述
```cpp

// Retrieved from C++Primer5, S.B.Lippman
#include <cstddef>
using std::size_t;

#include <vector>
using std::vector;

#include <iostream>
using std::cin;
using std::cout;
using std::endl;

#include <iterator>
using std::cbegin;
using std::cend;

// 注意上面的写法, 用不同的include区分各自的类成员
// 我们很清晰地知道, size_t在<cstddef>里面, vector在<vector>里面, 而各种流对象cin, cout,和流操作子endl在<iostream>里面.

// 有点奇怪, grade一般指"等级", 也就是 A,B,C这样子, 而score一般指具体的分数, 也就是97,87,77这样子
// 那么这个命名就出现问题了!!, 应该是vector<unsigned> scores才对! 而后面的grades应该才是进行++的对象!!


int main ()
{
	vector<unsigned> grades;
	// count the number of grades by clusters of ten:
	// 就是以10分为一个cluster(可以直接理解为一个group, 分成小组), 然后统计落在各个区间(小组)的人数
	// 0--9, 10--19, . . . 90--99, 100, 一共11个小组.
	const size_t sz = 11;
	unsigned scores[sz] = {};  // 11 buckets, all value initialized to 0,
	// 疑问, 是什么实现了数组的自动初始化呢?
	// 这个scores应该命名为 numOfStudentsInDifferentClusters更好.
	unsigned grade;
	// 你们传参的时候, 可以传一些-1,-2什么的, 观察下溢出, 很好玩的.
	while (cin >> grade) {
		if (grade <= 100)
			// 这边不用限制 负数 或者 字母 的情况, 因为这个在grade定义为unsigned的时候已经处理好了
			// increment the counter for the current cluster
			++scores[grade/10];
		// grade/10 由于是截断除法, 所以可以覆盖从0-10共11个indices
		// 这边的scores相当于numOfStudentsInDifferentClusters, 在特定的分数段增加一个人的计数(++)
		grades.push_back(grade);
		// push_back相当于append, push_head就相当于append_head
	}
	cout << "grades.size = " << grades.size() << endl;
	// 这个地方顺便一提: size()是运行时确定的, 而sizeof()是编译时确定的.

	// for every element in grades
	// C++05中对于string类和各种容器类（如vector等）添加了T.begin()和T.end()两个成员函数,
	// 于是遍历容器的办法就变成了都用迭代器了, 当然这样我们是很开心的.

	// 个人建议所有的iterator迭代器全部用auto声明比较好, 因为类型名字太长了
	for (vector<unsigned>::const_iterator g = grades.begin(); g != grades.end(); ++g)
		// 使用迭代器g对grades数组进行遍历, 迭代器也可以++(说明++也进行了重载)
		cout << *g << " " ;
	// 迭代器本质上是一个指针, 但是因为能够使用begin()和end()方法, 所以不用担心越界, 因此更加安全
	// 尽量使用迭代器去遍历数组, 因为这样更加安全.
	// 做一个专题, 就是cpp的5类迭代器.
	cout << endl;

	// for each counter in scores
	// 这个时候原生数组就比较弟弟了, 因为数组不是类类型
	// (数组array并不是容器或者string, 更加底层所以没有做T.begin()和T.end()的实现, 与C兼容也是其中一部分考虑)
	// 看看这里, 单纯为了找一个好的"临时变量类型"就得引入一个size_t, 虽然C语言的确一般都是这么做的, 但是C++这么做就显得非常awkwar了
	for (size_t i = 0; i != sz; ++i)
 	// 这么写太搞笑了, 堂堂C++Primer这么写代码(可能是为了体现容器类型与普通数组的区别, 但其实可以换种方式实现)
		cout << scores[i] << " ";       // print the value of that counter
	cout << endl;

	// 我自己的"遍历普通数组"的实现如下:引入<iterator>

	// 这里cbegin()是因为我想做一个直接得到const, 防止一些乱七八糟的问题
	auto array_first=cbegin(scores);
	// 我也不管你前面用什么类型来做数组下标的, 反正涉及到迭代一律auto走起,
    // 因为我后续肯定也不需要用到这两个临时变量了, 所以使用auto合情合理.
    // 一点猜想, 此处类型应该是const size_t*, 我使用const size_t*, 编译是OK的
    const size_t* array_last=cend(scores);

	// 注意这里因为array_first和array_last已经进行过类型声明了, 所以不是for(auto ..)
	// 很多人有个误区呀, 就是觉得for的条件与传参类似, 实际上大错特错,
	// for里面的这个stmts实际就是普通的变量定义与变量赋值而已, 只是它的位置比较特殊, 他放在for的stmt里面
	// 但是函数传参不一样, 函数传参本质上是内部实现stack_frame时候需要的一个参数表
	// 这么举例, 就是for语句后面跟的就是普通的赋值语句, 跟的是很多个expressions组成的stmts, 所以它是使用分号隔开的
	// 而函数传参, 因为是传一个参数表, "实际上可以理解为传入一个有很多形参的元组"(学过Haskell的人就知道), 而元组是使用逗号隔开的
	// 所以函数传参和for循环搞不清楚到底用分号还是逗号的, 本质上就是没有把握住这个历史脉络, 还是想得太少了

	for(array_first;array_first!=array_last;array_first++){
		cout << *array_first << " ";
	}

	cout << endl;
    return 0;
}
```
## 参考
- [强推!!-迭代器与指针的区别](`https://web.archive.org/web/20220605115854/https://www.zhihu.com/question/54047747/answer/137755282`)
- [C++五种迭代器](`https://web.archive.org/web/20220605114953/https://blog.csdn.net/sim_szm/article/details/8980879`)
- [C++迭代器遍历数组与容器](`https://web.archive.org/web/20210315030549/https://blog.csdn.net/qq_37653144/article/details/78552479`)
- [wiki-C++迭代器](`https://web.archive.org/web/20220605120507/https://zh.wikibooks.org/zh-hans/C++/STL/Iterator`#5个作为iterator_tag的空类)

