## 损失函数

### 1、0-1损失函数
<div align=center><img width="900" height="100" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/0-1_lossfunction.png"/></div>

### 2、绝对值损失函数
$L(y,\hat{y})=|y-\hat{y}|$

### 3、对数损失函数
$L(Y,P(Y|X))=-logP(Y|X)$
- 特点：①能非常好的表征概率分布，在多分类中，若需知道结果属于每个类别的置信度，比较合适；②鲁棒性不强；③逻辑回归的损失函数就是log对数损失函数

### 4、平方损失函数
$loss=\sum_{N}^{}(y-\hat{y})^2$
- 经常应用于回归问题

### 5、指数损失函数
$loss=e^{-y\cdot \hat{y}}$

### 6、Hinge损失函数
loss=max(0,1-yf(x))
- 特点：①表示如果被分类正确，损失为0，否则损失为$1-y\hat{y}$,SVM就是使用这个损失函数；②鲁棒性较高，对异常点，噪声不敏感

### 7、交叉熵损失函数
$C=-\frac{1}{n}\sum_{x}^{}[yln\hat{y}+(1-y)ln(1-\hat{y})]$，其中$x$是样本，$y$是真实标签，$\hat{y}$是预测输出，$n$是样本总量
- 特点：①本质是一种对数似然函数，可用于二分类和多分类中；②当使用sigmoid作为激活函数时，常用交叉熵损失函数而不用均方差损失函数，因为它可以完美解决平方损失函数权重更新过慢的问题，具有“误差大的时候，权重更新快；误差小的时候，权重更新慢”的良好性质
