#   #include防范

### 作用

>  防止引入错误。
>
> 比如a.h 中定义一个struct
>
> b.h 使用了`#include a.h`
>
> c.h 使用了`#include a.h     #include b.h`
>
> 此时编译c.h会出错

### 方法：

1. 使用`#ifndef xxx`，提供预编译选项

   > `ifndef = if not defined`
   >
   > ```c++
   > #ifndef H_xxxx
   > #define H_xxxx
   > 
   > #endif
   > ```
   >
   > 即每次引入该文件时，检查`H_xxxx`宏变量，当其不存在时，才继续进行，否则直接进行#endif

2. 使用`#pragam once`

   > 也可以保证该文件只被引入一次。
   >
   > 是个非标准的方法，建议使用1中的方法

### Feference

> https://zh.wikipedia.org/wiki/Include%E9%98%B2%E7%AF%84

