## 安装

### 于Ubuntu16.04
&emsp;&emsp;1、安装CUDA、cudnn

&emsp;&emsp;2、安装Anaconda

&emsp;&emsp;[点这里下载](https://www.anaconda.com/products/individual)

&emsp;&emsp;3、创建虚拟环境
```
conda create -n tf     #创建环境
source activate tf     #进入环境
source deactivate tf   #退出环境
```
&emsp;&emsp;4、安装TensorFlow的GPU版
```
conda install tensorflow-gpu
```
&emsp;&emsp;5、检验是否安装成功

&emsp;&emsp;终端进入python看能否导入tensorflow包成功，不报错即可
```
import tensorflow as tf
```
