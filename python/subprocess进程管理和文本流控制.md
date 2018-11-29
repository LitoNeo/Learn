## **subprocess**

简述:

> 1. 用于子进程的创建和管理(拥有多个创建子进程的函数供不同方式的调用)
> 2. 管理`标准流(std)`和`管道(pipe)`的工具

#### 1. 子进程管理

(1). `subprocess.call()`用于创建子进程,返回退出信息(0表示成功)

(2). `subprocess.check_call()`除创建子进程外和返回退出信息外,还会主动对返回信息进行检查,错误则举出`subprocess.CalledProcessError`错误提示(可用try...except检查)

(3). `subprocess.check_output()` 检查子程序的标准输出结果

##### 关于.call()的参数:

> call的参数当中含有`shell=boll`,用于指示是否调用系统的shell来执行(shell=True时)
>
>call的参数传递可以直接`call("ls -al",shell=True)`或者`call(['ls','-al'])`

##### 关于父进程是否等待子进程完成:

```python
child = subprocess.call(command)
child.wait()	# 如果不添加child.wait(),父进程将继续执行下去,而不等待子进程完成
print "child process finished"
```

##### 关于子进程的管理:

```python
child.poll()	# 检查子进程状态
child.send_signal()	# 向子进程发送信号(int)
child.kill()	    # 终止子进程
child.terminate()	# 终止子进程
```

#### 2.文本流控制

文本流包括`stdin stdout stderr`

##### 创建Popen对象

`res = subprocess.Popen(cmd, shell=True,stdin=child1.stdout, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)`

如上,可以讲Popen对象的输入输出重定向(比如重定向到PIPE),从而进行进程间的通信



