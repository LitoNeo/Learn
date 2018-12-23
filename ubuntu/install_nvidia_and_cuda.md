## Ubuntu os: Install NVIDIA-drivers and CUDA

### NVIDIA-driver

> 1. with `.runfile` method
>
>    1) download  the right driver 
>
>    2) `Ctrl+Alt+F1` to enter the cmd screen
>
>    3) uninstall prior driver
>
>    ​	`sudo apt-get remove --purge nvidia*`
>
>    4) sudo chmod a+x NVIDIA-Linux-x86_64_xxxx.run
>
>    5) sudo ./NVIDIA-Linux-x86_64-375.20.run  -no-x-check  -no-nouveau-check   -no-opengl-files
>
>    > -no-x-check  : to make sure the X service is shut down while installing nvidia driver
>    >
>    > -no-nouveau-check : to make sure the nouveau is forbidden while installing 
>    >
>    > -no-opengl-files: only install driver files , without openGL files
>
> 2. with `apt-get install` method
>
>    1) uninstall prior driver
>
>    ​	`sudo apt-get remove --purge nvidia*`
>
>    2) if the source origin haven't been added in software-source:
>
>    ​	`sudo add-apt-repository ppa:graphics-drivers`
>    ​	`sudo apt-get update`
>
>    3) find the recommanded nvidia-driver by ubuntu:
>
>    ​	`ubuntu-drivers devices`
>
>    4) install
>
>    ​	`sudo apt-get install nvidia-390 nvidia-settings nvidia-prime`
>
> 3. CHECK if the driver is correctly installed
>
>    1) `lsmod | grep nvidia` 
>
>    ​	if no output,then failed
>
>    2) `lsmod | grep nouveau`
>
>    ​	if there is no output, then success
>
>    3) (optional) Forbid local driver update
>
>    ​	`sudo apt-mark hold nvidia-xxx`

Reference: https://blog.csdn.net/breeze5428/article/details/80013753

CUDA (9.0)

[]: http://www.zhimengzhe.com/bianchengjiaocheng/qitabiancheng/415560.html	"CUDA install: Reference"

