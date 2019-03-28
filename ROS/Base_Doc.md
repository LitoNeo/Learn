## 基本的ROS知识

---
### 1. Error: couldnot find AF_INET....
一般这个错误有两个原因:
> 1. ROS_master的IP设置的不对,到 .bashrc里看看有没有重设master_ip  --(暂时没遇到过这个问题)
> 2. NodeHandle在ros::init()之前被定义
> >注意:除了显示的ros::NodeHandle, **tf::broadcaster等也是NodeHandle**

### 2. ros::Subscriber中的回调函数可以接受多个参数,使用bind进行绑定
参考: http://www.cnblogs.com/TIANHUAHUA/p/8418818.html

### 3. dynamic_reconfiguration运行时动态调参数
具体的用法参考官方的wiki即可--> http://wiki.ros.org/dynamic_reconfigure/Tutorials
> .cfg文件中最后的`exit(gen.generate(PACKAGE, "dynamic_tutorials", "Tutorials"))`
> * PACKAGE表示该cfg文件作用的`包名`  
> * 第二个参数表示cfg文件作用的`节点名`  
> * 第三个参数表示cfg文件生成的`头文件名前缀` --实际用以引入的头文件名为`prefix`+`Config.h`


~~注: 暂时没有找到在类中定义/使用动态reconfiguration的方法, 因此最好不要将reconfiguration写到类中~~ -->**Yes, you can do it now**
使用boost::bind(&func,_1,_2,params)绑定多个参数,即将类的实例作为参数传入到func中.
**以ray_ground_filter的实现为例:**
* 在类中定义
```c++
void RayGroundFilter::reset_params(const ray_ground_filter::RayFilterConfig& config){
    SENSOR_HEIGHT = config.sensor_height;
    // and others
}
```
* 在`main`函数所在的主文件中定义
```c++
void cfg_handle(const ray_ground_filter::RayFilterConfig& config, uint32_t level, RayGroundFilter* filter)
{
    filter->reset_params(config);
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "ray_ground_filter_node");
    ros::NodeHandle nh_("~");

    RayGroundFilter filter(nh_); // 实例化对象
    filter.run();

    dynamic_reconfigure::Server<ray_ground_filter::RayFilterConfig> cfg_server;
    dynamic_reconfigure::Server<ray_ground_filter::RayFilterConfig>::CallbackType cfg_callback = boost::bind(&cfg_handle, _1, _2, &filter);
    cfg_server.setCallback(cfg_callback);

    ros::spin();
    return 0;
}
```
**分析**
如上在`main`函数中,`cfg_callback`绑定了`一个函数,三个参数`  
> `boost::bind(&cfg_handle, _1, _2, &filter)`
> * &cfg_handle为绑定的函数,该函数有三个参数(config,level, filter)
> * `_1,_2`为`占位符`, 因为`cfg_server`本身会传入两个参数,分别作为cfg_handle的第一第二个参数
> * `&filter`是第三个参数,该参数`不使用占位符,直接传入`

* 注:不可使用`boost::bind(&filter.reset_params, _1, _2)`这种形式,该形式无法编译通过
* 上述流程`main ->boost::bind本地函数(多参数) ->本地函数修改类中参数`以后直接套用  

**附:c++的 值传递 指针传递 引用传递**
* 值传递 就是复制传递,不影响原参数
* 指针传递:(**类的实例作为参数传入函数时,只有使用指针传递才能改变实例中的变量!!!**)
> * 定义时使用 * ,如上`cfg_handle`中`RayGroundFilter* filter`
> * 使用时使用 & ,如上`cfg_callback`绑定时第三个参数`&filter`
> * 正统描述: 形参为指向实参地址的指针，当对形参的指向操作时，就相当于对实参本身进行的操作
* 引用传递(**类的实例使用引用传递传入函数时,并不能改变实例中的参数!!**)
> * 定时时使用 & 
> * 使用时直接使用原参数,不加&等取地址符号
> * 形参相当于是实参的“别名”
> * 对形参的操作其实就是对实参的操作，在引用传递过程中，被调函数的形式参数虽然也作为局部变量在栈中开辟了内存空间，但是这时存放的是由主调函数放进来的实参变量的地址。被调函数对形参的任何操作都被处理成间接寻址，即通过栈中存放的地址访问主调函数中的实参变量。正因为如此，被调函数对形参做的任何操作都影响了主调函数中的实参变量。
* 指针传递和引用传递的区别
[参考](https://www.cnblogs.com/yanlingyin/archive/2011/12/07/2278961.html)
- [ ] TODO::还要继续加深理解
