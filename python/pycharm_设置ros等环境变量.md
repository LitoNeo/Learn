# pycharm设置环境变量

pycharm 不会自动导入系统的环境变量,需要单独进行设置

以pycharm设置ros环境变量为例

1. 在`/usr/share/applications/`或者`~/.local/share/applications/`下找`jetbrains-xxxxx.desktop`(注意:名字可能不一样,使用Tab进行补全.该文件并非新建,而是在安装pycharm时候已经存在的)

   > `Exec=bash -i -c /home/sin/soft/pycharm-2018xx/bin/pycharm.sh` 

2. 直接在pycharm中设置

> 好像是在Run->Debug->Edit Configuration->Configuration->Environment variable中添加PYTHONPATH变量，加入ros相关路径。没试过.

