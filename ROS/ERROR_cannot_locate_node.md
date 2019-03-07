## ROS Error: Cannot locate node of type xxxxx

### 原因1: 同一workspace下有同名包, 改成不同名即可

参考: https://www.jianshu.com/p/e9981bc35cff

> 可使用 catkin_find --without-underlays --libexec --share  <pkg-name>   查找

### 原因2: `CMakeLists.txt`里漏写`catkin_package()`

> 真是一个有趣的错误...
>
> 漏写该语句导致`catkin_make`命令无法正确生成可执行文件