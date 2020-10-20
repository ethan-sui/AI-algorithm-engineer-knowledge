## 回归框损失

&emsp;&emsp;近些年的发展SmoothL1 loss → IoU loss(2016) → GIoU loss(2019) → DIoU loss(2020) → CIoU loss(2020)

1、SmoothL1 loss
<div align=center><img width="500" height="260" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/smoothl1_loss.jpg"/></div>

&emsp;&emsp;当预测框与gt误差较小时，有较低的梯度变化，可以使框预测更精准

&emsp;&emsp;PS：对于框的预测是个回归问题，回归问题通常可选择L2损失，但这个损失对于比较大的误差的惩罚很高，那采用稍微缓和一些的绝对值函数L1损失，但是这个函数在0处不可导，因此可能会影响收敛，所以采用Smooth L1损失

2、$IoU loss=1-IoU=1-\frac{A\cap B}{A\cup B}$
<div align=center><img width="500" height="130" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/IoUloss.PNG"/></div>
&emsp;&emsp;问题：

&emsp;&emsp;①、图a所示，当预测框与gt不相交时，IoU=0，无法反应两个框距离的远近，此时损失函数不可导，即无法优化两个框不相交的情况

&emsp;&emsp;②、如b、c所示，两个预测大小相同，IoU也相同，但是IoU_loss无法区分两者相交位置的不同

3、$GIoU loss=1-GIoU=1-(IoU-\frac{差集}{C})$
<div align=center><img width="500" height="130" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/GIoUloss.PNG"/></div>

&emsp;&emsp;GIoU增加了相交尺度的衡量，但是当出现如a、b所示情况时，预测框和gt的差集都是相同的，因此这三种状态的GIoU值也都是相同的，这时GIoU就退化到了IoU

4、$DIoU loss=1-DIoU=1-(IoU-\frac{Distance\_2}{Distance\_c})$
<div align=center><img width="500" height="130" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/DIoUloss.PNG"/></div>

&emsp;&emsp;直接度量两个框的中心距离，解决了预测框与gt重叠的问题，但是如a、b所示，会有不同宽高比的框无法度量的问题

5、$CIoU loss=1-CIoU=1-(IoU-\frac{Distance\_2}{Distance\_c}-\frac{v^{2}}{(1-IoU)+v})$

&emsp;&emsp;CIoU比DIoU改进增加了一个影响因子，将预测框与目标框的长宽比都考虑进去了，其中v是衡量长宽比一致性的参数，定义为：

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;$v=\frac{4}{\pi ^{2}}(arctan\frac{w^{gt}}{h^{gt}}-arctan\frac{w^{p}}{h^{p}})^{2}$

&emsp;&emsp;CIoU考虑了三个重要的几何因素：重叠面积、中心点距离、长宽比
