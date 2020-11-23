## 激活函数
- 激活函数就是一个非线性函数，可以将非线性模式转化为线性模式
- 特性：非线性，几乎处处可微，有非饱和性，单调性，输出范围有限
- 作用主要就是增加非线性，提高模型的表征能力
- 常见的激活函数

### 1、Sigmoid
<div align=center><img width="300" height="220" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/Sigmoid.png"/></div>

&emsp;&emsp;表达式：$sigmoid(x)\frac{1}{1+e^{-x}}$

&emsp;&emsp;特点：可解释，比如将0-1之间的取值解释成一个神经元的激活率

&emsp;&emsp;缺点：①梯度消失，当输入为大的正数或者负数时，梯度为0，使得神经元基本不能更新；②不是零中心激活函数，输出全为正数，会导致zigzag现象；③有指数计算，计算量偏大

### 2、tanh
<div align=center><img width="300" height="220" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/tanh.png"/></div>

&emsp;&emsp;表达式：$tanhx=\frac{(e^{x}-e^{-x})}{(e^{x}+e^{-x})}$

&emsp;&emsp;和sigmoid类似，仅仅时尺度和范围不同，也是有饱和区，也会出现梯度消失，改进的一点是，变为了零值对称激活函数，不会出现zigzag现象，能更快收敛

### 3、ReLU(整流线性单元)
<div align=center><img width="300" height="220" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/ReLU.png"/></div>

&emsp;&emsp;卷积神经网络中常用到，是一个分段激活函数

&emsp;&emsp;公式：$f(x)=max(0,x)$

&emsp;&emsp;优势：①计算复杂度低，没有指数计算，比sigmoid、tanh收敛更快；②在x>0的区域，不会出现梯度消失和梯度饱和现象

&emsp;&emsp;缺点：①ReLU的输出不是零均值的；②会出现神经元坏死现象(dead relu)，在x<0时，梯度为0。这个神经元及之后的神经元梯度永远为0，不再对任何数据有所响应，导致相应参数永远不会被更新

### 4、Leaky ReLU(渗漏整流线性单元)
<div align=center><img width="300" height="220" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/Leaky%20ReLU.png"/></div>

&emsp;&emsp;为了解决ReLU的dead relu现象提出的，保证了x<0区域输出不为0，0.01是经验值，是一个超参数

&emsp;&emsp;公式：$f(x)=max(0.01x,x)$

### 5、PReLU(参数整流线性单元)
&emsp;&emsp;同Leaky ReLU基本一样，但是不一样的是将Leaky ReLU的超参数通过网络学习出来的，不需要预先给值，这样学习出来的权重可能会更合适，但是计算也会相应更复杂一些

&emsp;&emsp;公式：$f(x)=max(\alpha x,x)$，其中$\alpha$就是学习出来的

### 6、ELU(指数线性单元)
<div align=center><img width="300" height="220" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/ELU.png"/></div>

&emsp;&emsp;我们发现前面的三个ReLU在0处是不可导的，所以ELU又在PReLU的基础上进行改进解决这个问题

&emsp;&emsp;公式:
<div align=center><img width="1500" height="80" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/ELU_function.png"/></div>

### 7、Maxout
&emsp;&emsp;Maxout是对ReLU和Leaky ReLU的一般化归纳

&emsp;&emsp;公式：$f(x)=max(w_{1}^{T}x+b_{1},w_{2}^{T}x+b_{2})$

&emsp;&emsp;优点：①Maxout的拟合能力非常强，可以拟合任意的凸函数；②Maxout具有ReLU的所有优点，线性、不饱和性。同时没有ReLU的一些缺点，如：神经元坏死

&emsp;&emsp;缺点：增加了更多的参数

### 8、Mish
<div align=center><img width="300" height="220" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/Mish.png"/></div>

&emsp;&emsp;较新的一个激活函数，有更好的平滑性，在论文中的对比也取得了不错的效果

&emsp;&emsp;公式：$Mish(x)=x×tanh(ln(1+e^{x}))$
