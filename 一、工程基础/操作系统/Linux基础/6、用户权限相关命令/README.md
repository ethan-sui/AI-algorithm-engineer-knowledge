## 用户权限相关命令
### 1、对文件/目录的权限
- 读(r)、写(w)、执行(x)

|目录|拥有者权限|组权限|其他用户权限|
|-|-|-|-|
| -| r w -| r w -| r - -|
| d| r w x| r w x| r - x|
### 2、组管理
- groupadd 组名 添加组
- groupdel 组名 删除组
- cat /etc/group 确认组信息
- chgrp 组名 文件/目录名 修改文件/目录的所属组
### 3、用户管理，终端命令
- useradd -m -g 组 创建用户名：添加新用户
- passwd 用户名：设置用户密码
- userdel -r 用户名：删除用户
- cat /etc/passwd | grep 用户名：确认用户信息
- id [用户名]：查看用户UID和GID信息
- who：查看当前所有登录的用户列表
- whoami：查看当前登录用户的账户名
- which：可以查看执行命令所在位置
- su -用户名：切换用户，并且切换目录
- exit：退出当前登录账户
### 4、修改文件权限
- chown：修改拥有者
- chgrp：修改组
- chmod：修改权限
