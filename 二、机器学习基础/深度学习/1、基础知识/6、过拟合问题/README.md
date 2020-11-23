## 基础知识
### 1、激活函数
- 激活函数就是一个非线性函数，可以将非线性模式转化为线性模式
- 特性：非线性，几乎处处可微，有非饱和性，单调性，输出范围有限
- 作用主要就是增加非线性，提高模型的表征能力
- 常见的激活函数

1、Sigmoid

<div align=center><img width="300" height="220" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/Sigmoid.png"/></div>

&emsp;&emsp;表达式：$sigmoid(x)\frac{1}{1+e^{-x}}$

&emsp;&emsp;特点：可解释，比如将0-1之间的取值解释成一个神经元的激活率

&emsp;&emsp;缺点：①梯度消失，当输入为大的正数或者负数时，梯度为0，使得神经元基本不能更新；②不是零中心激活函数，输出全为正数，会导致zigzag现象；③有指数计算，计算量偏大

2、tanh

<div align=center><img width="300" height="220" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/tanh.png"/></div>

&emsp;&emsp;表达式：$tanhx=\frac{(e^{x}-e^{-x})}{(e^{x}+e^{-x})}$

&emsp;&emsp;和sigmoid类似，仅仅时尺度和范围不同，也是有饱和区，也会出现梯度消失，改进的一点是，变为了零值对称激活函数，不会出现zigzag现象，能更快收敛

3、ReLU(整流线性单元)

<div align=center><img width="300" height="220" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/ReLU.png"/></div>

&emsp;&emsp;卷积神经网络中常用到，是一个分段激活函数

&emsp;&emsp;公式：$f(x)=max(0,x)$

&emsp;&emsp;优势：①计算复杂度低，没有指数计算，比sigmoid、tanh收敛更快；②在x>0的区域，不会出现梯度消失和梯度饱和现象

&emsp;&emsp;缺点：①ReLU的输出不是零均值的；②会出现神经元坏死现象(dead relu)，在x<0时，梯度为0。这个神经元及之后的神经元梯度永远为0，不再对任何数据有所响应，导致相应参数永远不会被更新

4、Leaky ReLU(渗漏整流线性单元)

<div align=center><img width="300" height="220" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/Leaky%20ReLU.png"/></div>

&emsp;&emsp;为了解决ReLU的dead relu现象提出的，保证了x<0区域输出不为0，0.01是经验值，是一个超参数

&emsp;&emsp;公式：$f(x)=max(0.01x,x)$

5、PReLU(参数整流线性单元)

&emsp;&emsp;同Leaky ReLU基本一样，但是不一样的是将Leaky ReLU的超参数通过网络学习出来的，不需要预先给值，这样学习出来的权重可能会更合适，但是计算也会相应更复杂一些

&emsp;&emsp;公式：$f(x)=max(\alpha x,x)$，其中$\alpha$就是学习出来的

6、ELU(指数线性单元)

<div align=center><img width="300" height="220" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/ELU.png"/></div>

&emsp;&emsp;我们发现前面的三个ReLU在0处是不可导的，所以ELU又在PReLU的基础上进行改进解决这个问题

&emsp;&emsp;公式:
<div align=center><img width="1500" height="80" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/ELU_function.png"/></div>

7、Maxout

&emsp;&emsp;Maxout是对ReLU和Leaky ReLU的一般化归纳

&emsp;&emsp;公式：$f(x)=max(w_{1}^{T}x+b_{1},w_{2}^{T}x+b_{2})$

&emsp;&emsp;优点：①Maxout的拟合能力非常强，可以拟合任意的凸函数；②Maxout具有ReLU的所有优点，线性、不饱和性。同时没有ReLU的一些缺点，如：神经元坏死

&emsp;&emsp;缺点：增加了更多的参数

8、Mish

<div align=center><img width="300" height="220" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/Mish.png"/></div>

&emsp;&emsp;较新的一个激活函数，有更好的平滑性，在论文中的对比也取得了不错的效果

&emsp;&emsp;公式：$Mish(x)=x×tanh(ln(1+e^{x}))$
### 2、损失函数

1、0-1损失函数
<div align=center><img width="900" height="100" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/0-1_lossfunction.png"/></div>

2、绝对值损失函数
$L(y,\hat{y})=|y-\hat{y}|$

3、对数损失函数
$L(Y,P(Y|X))=-logP(Y|X)$
- 特点：①能非常好的表征概率分布，在多分类中，若需知道结果属于每个类别的置信度，比较合适；②鲁棒性不强；③逻辑回归的损失函数就是log对数损失函数

4、平方损失函数
$loss=\sum_{N}^{}(y-\hat{y})^2$
- 经常应用于回归问题

5、指数损失函数
$loss=e^{-y\cdot \hat{y}}$

6、Hinge损失函数
loss=max(0,1-yf(x))
- 特点：①表示如果被分类正确，损失为0，否则损失为$1-y\hat{y}$,SVM就是使用这个损失函数；②鲁棒性较高，对异常点，噪声不敏感

7、交叉熵损失函数
$C=-\frac{1}{n}\sum_{x}^{}[yln\hat{y}+(1-y)ln(1-\hat{y})]$，其中$x$是样本，$y$是真实标签，$\hat{y}$是预测输出，$n$是样本总量
- 特点：①本质是一种对数似然函数，可用于二分类和多分类中；②当使用sigmoid作为激活函数时，常用交叉熵损失函数而不用均方差损失函数，因为它可以完美解决平方损失函数权重更新过慢的问题，具有“误差大的时候，权重更新快；误差小的时候，权重更新慢”的良好性质

### 3、卷积神经网络的结构
1、输入层

&emsp;&emsp;卷积网络的原始输入，可以是原始或预处理后的像素矩阵

2、卷积层

&emsp;&emsp;参数共享，局部连接，利用平移不变性从全局特征提取局部特征

3、激活层

&emsp;&emsp;将卷积层的输出结果进行非线性映射

4、池化层

&emsp;&emsp;进一步的筛选特征，可以有效的减少后续网络层次所需的参数量

5、全连接层

&emsp;&emsp;将多维特征展平为二维特征，通常低纬度特征对应任务的学习目标

### 4、反向传播
&emsp;&emsp;计算出输出与标签间的损失函数值，然后计算其相对于每个神经元的梯度，根据梯度方向更新权值

&emsp;&emsp;(1)、将训练集输入到网络的输入层，经过隐藏层，最后达到输出层并输出结果，这是模型的前向传播过程

&emsp;&emsp;(2)、由于网络的输出结果与实际结果有误差，则计算估计值与实际值之间的误差，并将该误差从输出层向隐藏层反向传播，直至传播到输入层

&emsp;&emsp;(3)、在反向传播的过程中，根据误差调整各种参数的值，不断迭代上述过程，直至收敛
### 5、BN层
&emsp;&emsp;在神经网络中，数据经过每一层时，都会有可能引起数据分布的变化，而使得收敛较慢，所有BN层的思路就是想着在每一层后面加一个标准化的擦欧总，再送入下一层进行学习，但如果只是简单的进行归一化，又可能会导致某些数据特征被破坏，比如某层使用ReLU激活函数，然后输入数据都落在0的左侧，那这个时候都被激活了，但如果使用标准化，那将有很多的参数跑到左侧，从而这部分特征就学不到了，所以BN层又使用了两个可学习的参数，来进行缓和，即
$y^{(k)}=\gamma ^{(k)}\hat{x}^{(k)}+\beta ^{(k)}$

### 6、过拟合问题
&emsp;&emsp;在训练集上表现良好，而在测试集上表现较差，这就是过拟合
- 防止过拟合的方法：

&emsp;&emsp;(1)、数据增广

&emsp;&emsp;(2)、使用Dropout降低模型复杂度

&emsp;&emsp;(3)、使用正则化，L1范数可以稀疏网络，一定程度上防止过拟合，L2范数可以降低对数据的敏感度，提高模型的泛化能力，更能防止过拟合

&emsp;&emsp;(4)、多任务学习，将任务分成多个小任务同时学习，模型最终认可的是多个任务的共同一致的表示，从而使得模型在原始任务上的过拟合风险变小
