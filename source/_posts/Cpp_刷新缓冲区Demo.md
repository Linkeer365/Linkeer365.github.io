---
title: Cpp_刷新缓冲区demo
tags:
abbrlink: 23454
date: 2019-08-06 00:36:45
---
本文不讨论buffer的功能, 单单演示buffer刷新的场景

- 思路:
    - cout和clog不刷缓冲区, endl与cerr一定会刷缓冲区(endl=\n+flush, \n只有在行缓冲情况下会flush)
    - 缓冲区和流需要用setvbuf()绑定, reasons尚不明
    - 缓冲区和流绑定后, 通过观察控制台输出的停顿, 模拟缓冲区行为, 得到缓冲区的直观概念

- cout不刷新缓冲区:

```cpp

#include <windows.h>
#include <iostream>

using namespace std;

int main()
{
    setvbuf(stdout, NULL, _IOLBF, 10);  
    //os指定为stdout,设置控制台输出为行缓存模式(L)，把缓冲区与流相关, 缓存区大小设为10字节
    for (int i = 0; i < 1000; ++i) { 
        cout << i; // 这里可以顺便设计一个重定向, 不必老盯着控制台
        Sleep(50);
        if (i%3==0)
            cout<<'\n'; //行缓冲, 遇到\n就刷新buffer[把缓存中的东西取出, 放到终端设备中]
    }
    return 0;
}
```


- endl刷新缓冲区

```cpp
#include <windows.h>
#include <iostream>

using namespace std;

int main(){
    setvbuf(stdout, NULL, _IOFBF, 1024);  //设置控制台输出为全缓存模式(F)，把缓冲区与流相关
    cout << "我会和最后一个cout一起出现\n";
    Sleep(500);
    cout << "我会和最后一个cout一起出现\n";
    Sleep(500);
    cout << "我是最后一个cout, 我们三个同时出现";

    cout << "----新一轮----"<< endl;
    cout << "我不会独自最先出现的";
    Sleep(500);
    cerr << "我是红色字, 我不会等, 还会连同前面cout一起刷出来\n";
    Sleep(500);
    cout << "有endl我就不等后面的cout了"<< endl;
    Sleep(500);
    cout << "有endl, 前面的cout会先输出" << endl;
    return 0;
}
```

- 总结
    - cout是一个os对象, 其实仅仅完成"放入缓冲区"这一功能, 要显示在显示器上还需要刷新缓冲区
    - 如果只有cout没有endl, 之所以会有输出是因为return 0;后会自动执行刷新, 不刷就根本不能显示
    - 把缓冲区当做一个"武器匣子"
        - 武器匣子执行"弹出"功能, 即弹出的武器是要拿来用的, 同时弹出的武器同时也从武器匣子中消除;
        - 武器匣子可能会塞不下, 此时自然有两种FIFO或FILO, 联系到ring buffer以及 stack buffer
