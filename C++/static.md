## static关键字总结

### 1. 隐藏  

### 	--即某个源文件的全局变量前加static会使得该变量为该源文件内的静态变量,外部不可访问

注:当同时编译多个文件时,所有未加static前缀的**全局变量和函数**都具有全局可见性

// 源a.cpp

```C++
char a = "A";
static char b = "B";
void msga(){
    cout<<a<<endl;
}
static void msgb(){
    cout<<b<<endl;
}
```

// 源b.cpp

```C++
int main(){
    extern a;
    cout<<a<<endl;  // 正常输出"A"  
    return 0;
}
```

但是源a.cpp中的b和函数msgb()由于加了static,因此源b中不可访问这两个元素

### 2. 保持变量内容的持久

​	-- static变量中的记忆功能和全局生存期

> 1. static声明的变量,只会在声明的时候进行初始化,后续任何操作都不会重新给static赋值 --这一点在循环函数可以很明显体现出来
>
>    ```C++
>    for(int i=0;i<10;i++){
>        static count = 10;
>        cout<<count<<endl;
>        count--;
>    }
>    // 以上函数会输出10 -- 1,即static count = 10 只会执行一次
>    ```

> 2. 同样static声明的变量存储在静态存储区,会生存在整个生存期,不会被消灭

### 3. static默认初始化变量为0

### 4. C++类中的static

> 1. 静态数据成员**是类的成员,而不是具化的对象的成员**
> 2. 待补充....