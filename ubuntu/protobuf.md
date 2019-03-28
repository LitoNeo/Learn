Reference: https://blog.csdn.net/qq_16775293/article/details/81119375

## 安装(兼容安装2个 和 覆盖安装)

### 1.两个版本protobuf兼容安装
Ubuntu 16.04 自带有 protobuf 2.6.1版本，如果想兼容的话按照下面方式安装 
1.1.1 下载并解压缩 
打开浏览器，输入地址：https://github.com/google/protobuf/releases/download/v3.4.1/protobuf-cpp-3.4.1.tar.gz    

(上述只包含c++ 的protobuf, 最好下载 `all` 版本的,包含python等)

1.1.2 解压安装包 
将下载后的包放在合适位置，右键Extract Here解压 
1.1.3 进入安装包目录，准备安装 
进入解压后的文件夹

`cd protobuf-3.4.1`

1.2 安装 
1）建议将protobuf安装在/usr/protobuf下。请先在/usr下新建一个名为protobuf的文件夹，此即为最终的安装路径。

`sudo mkdir /usr/protobuf`
2）执行以下命令：（执行下面第一句话时若不成功，则需要安装automake工具--`sudo apt-get install autoconf`即可）

```
./autogen.sh
./configure.sh --prefix=/usr/protobuf
make
make check
sudo make install
```

3)  配置

`sudo vim /etc/profile
`
在/etc/profile中添加下面内容

```
####### add protobuf lib path ########
#(动态库搜索路径) 程序加载运行期间查找动态链接库时指定除了系统默认路径之外的其他路径
`export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/protobuf/lib/`
#(静态库搜索路径) 程序编译期间查找动态链接库时指定查找共享库的路径
`export LIBRARY_PATH=$LIBRARY_PATH:/usr/protobuf/lib/`
#执行程序搜索路径
`export PATH=$PATH:/usr/protobuf/bin/`
#c程序头文件搜索路径
`export C_INCLUDE_PATH=$C_INCLUDE_PATH:/usr/protobuf/include/`
#c++程序头文件搜索路径
`export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/usr/protobuf/include/`
#pkg-config 路径
`export PKG_CONFIG_PATH=/usr/protobuf/lib/pkgconfig/`
######################################
```



1.3 安装完成 

保存退出/etc/profile。此时，最好重启电脑。
--------------------- 



### 2. 覆盖安装

2.1.1 下载并解压缩 
打开浏览器，输入地址：https://github.com/google/protobuf/releases/download/v3.4.1/protobuf-cpp-3.4.1.tar.gz 
2.1.2 解压安装包 
将下载后的包放在合适位置，右键Extract Here解压 
2.1.3 进入安装包目录，准备安装 
进入解压后的文件夹

$ cd protobuf-3.4.1
1
2.2默认安装步骤(需root权限) 
（不采用此种方法，因为会与ROS中的老版本的protobuf产生冲突）

```
$ ./autogen.sh    ##下载自github的代码需要执行此行来生成configure文件
$ ./configure
$ make
$ make check
$ make install
```



此时，protobuf会被安装到usr/local/bin，usr/local/lib，usr/local/include三个目录下。
--------------------- 



#### 注:如果要在python中使用protobuf, 还需要单独安装protobuf的python模块

> 1. 下载 wget <https://github.com/google/protobuf/releases/download/v3.6.0/protobuf-python-3.6.0.tar.gz>   (自行修改版本号)
>
> 2. cd ./python
> 3. python setup.py build
> 4. python setup.py test
> 5. python setup.py install

完成后进入python, 使用`import google.protobuf` 验证






## protobuf测试

测试protobuf是否安装成功： (以上安装完成后,需要重启电脑才能生效)
在/usr/protobuf中查看是否生成了bin,lib,include这3个文件夹。 
在终端输入

```
$ protoc --version
```

能查看到版本信息，输入which protoc能查看到安装路径。

## protobuf使用

4.1 在我们所写的程序中的include文件夹下，创建`.proto`文件。

4.2 将`/usr/local/protobuf/bin/`目录下的`protoc程序`复制到该include文件夹下。

4.3 在该include文件夹下打开终端执行以下命令，生成C++版本的协议文件。

```
$ ./protoc -I=./ --cpp_out=./ test.proto
```


注：test.proto是要编译的文件名。 
执行成功后，可以在当前目录下看到.h和.cc文件，之后就可以在我们的程序中使用生成的.h和.cc文件来序列化和反序列化消息了。

4.4使用protobuf写好ROS程序后，需要在CMakeLists.txt文件中添加下面两句

```
##use protobuf
INCLUDE_DIRECTORIES(/usr/protobuf/include/)
LINK_DIRECTORIES(/usr/protobuf/lib/)

```



注意：要在以下include这句之前加上!顺序不对将导致错误

```
# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)
```



同时，在使用到了protobuf的ROS节点上添加protobuf，如下

```
add_executable(recv src/recv.cpp)
target_link_libraries(recv
	${catkin_LIBRARIES}
	zmq
	protobuf
)
```

