## .hpp file

`.hpp`文件可以认为是将 .h文件和.cpp文件写到了一起, 因此函数的定义和实现都可以在一个hpp文件里.

> 这一特性使得.hpp文件非常适合于书写共享script文件

### 注意点:

使用共享 `.hpp`文件容易产生`multiple defination of xxx`错误, 这一错误是由于对同一变量的多次声明造成的.因此以下几点需要注意:

> 1. hpp文件中**不能包含有全局对象或全局函数**, 因此在引入hpp文件后, 引入的hpp和原文件很容易有相同变量名的变量,从而导致冲突.(编译不出错,但是链接出错)
>
> 2. 必须加条件编译, 避免一大批低级错误(包括.h文件里)
>
>    ```c++
>    #ifndef TEST_H
>    #define TEST_H
>    #endif
>    ```
>
> 3. hpp文件里定义的类不用写声明了, 类中直接写定义.(参见smartcat项目utils模块下的filter_ground.hpp, 将类中函数的声明和定义写到一起后, 解决multiple defination问题)
>
> 4. 其他情况可能产生该错误,具体待查

