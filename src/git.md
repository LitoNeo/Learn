# git

### 1. 获取远程分支内容

> #### (1) 通过切换分支来获取
>
> ```shell
> git glone git:xxxxx      # 一次性拖取远程库
> git checkout -b <local_branch_name> origin/<remote_branch_name>  # 新建本地分支，并与目标远程分支关联
> git checkout <local_branch_name>	# 切换到本地分支，done
> ```
>
> #### （2）直接拖取