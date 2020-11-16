## 其他命令
### 1、查找文件
- find [路径] -name ".py"：查找指定路径下拓展名是.py的文件，包括子目录
### 2、软链接
- ln -s 被链接的源文件(源文件要使用绝对路径) 链接文件：建立文件夹的软链接，类似于win下的快捷方式
### 3、打包压缩
- 打包文件：tar -cvf 打包文件.tar 被打包的文件/路径
- 解压文件：tar -xvf 打包文件.tar
- 压缩文件：tar -zcvf 打包文件.tar.gz 被压缩的文件/路径
- 解压缩文件：tar -zxvf 打包文件.tar.gz
- 解压缩到指定路径：tar -zxvf 打包文件.tar.gz -C 目标路径
### 4、软件安装
- 安装软件：sudo apt install 软件包
- 卸载软件：sudo apt remove 软件包
- 更新已安装的包：sudo apt upgrade
