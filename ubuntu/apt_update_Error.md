错误:

```
Reading package lists... Done                                                                                                
E: Failed to fetch http://mirrors.ustc.edu.cn/ubuntu/dists/xenial/main/binary-arm64/Packages  404  Not Found [IP: 202.38.95.110 80]
E: Failed to fetch http://mirrors.ustc.edu.cn/ubuntu/dists/xenial-security/main/binary-arm64/Packages  404  Not Found [IP: 202.38.95.110 80]
E: Failed to fetch http://mirrors.ustc.edu.cn/ubuntu/dists/xenial-updates/main/binary-arm64/Packages  404  Not Found [IP: 202.38.95.110 80]
E: Failed to fetch http://mirrors.ustc.edu.cn/ubuntu/dists/xenial-proposed/main/binary-arm64/Packages  404  Not Found [IP: 202.38.95.110 80]
E: Failed to fetch http://mirrors.ustc.edu.cn/ubuntu/dists/xenial-backports/main/binary-arm64/Packages  404  Not Found [IP: 202.38.95.110 80]
E: Some index files failed to download. They have been ignored, or old ones used instead.

```

该错误多是在换源之后出现的,会导致正常的软件无法安装.

原因:

> 注意错误提示中的这一句 `or old ones used instead` 
>
> 即系统中有旧版本的xx,没有删除,影响了源,因此删除即可

删除相应的old xx即可

比如示例中的错误,可执行:

> `sudo apt-get remove .*:arm64`
>
> `sudo dpkg --remove-architecture arm64`

