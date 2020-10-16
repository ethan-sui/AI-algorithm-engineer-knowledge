## 目标检测

###  1、目标检测的指标
- TP：真正例；FP：假正例；TN：真反例；FN：假反例
- 准确率(Accuracy)，指所有测试用例中，预测正确的比例，即$\frac{T}{T+N} $
$$Accuracy=\frac{TP+TN}{TP+FP+TN+FN}$$
- 召回率(Recall)，指预测出来的正例占所有正例的比例
$$Recall=\frac{TP}{TP+FP}$$
- 精确率(Precision)，指预测出来的真正例占所有预测为真例的比例
$$Precision=\frac{TP}{TP+FN}$$
- F1-score，是基于召回率和精确率的调和平均
$$F1-score=\frac{2Recall·Precision}{Recall+Precision}$$
- P，PR曲线下的面积
- mAP，数据集中所有类别AP的平均值

### 2、Anchor
&emsp;&emsp;anchor就是一系列的锚框，对于目标检测，不同的目标检测具有不同的宽高比，比如球类目标，可以用正方形框检测，而串或者筷子这种就可能需长方形矩形框来检测，所以有贴合于数据集的anchor会有较好的效果

&emsp;&emsp;anchor跟训练数据集有关，是通过K-means在数据集上聚类出来的，假设有如图所示数据集，我需要统计数据集中的高和宽以及宽高比，来进行聚类
<div align=center><img width="500" height="160" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/anchor01.PNG"/></div>

### 3、小目标的检测问题
&emsp;&emsp;在coco数据集中，面积小于32*32的物体都被认为是小目标
- 小目标难检的原因：分辨率低，图像模糊，携带的信息少，由此所导致特征表达能力弱，也就是提取的特征少
- 解决方案

&emsp;&emsp;1. 提升图像采集的分辨率或者模型的输入分辨率，但是也会导致更长的训练时间

&emsp;&emsp;2. 跟YOLO一样采用多尺度预测，不只是在最后预测，浅层阶段也要预测，而这时感受野较小，有利于小目标检测

&emsp;&emsp;3. 增加小目标的数量：①采集小目标多的数据；②在原图复制多个小目标

&emsp;&emsp;4. 对于小目标可以选择不苛刻的阈值，比如在NMS过程中

&emsp;&emsp;5. 在标注训练集时，适量增大小目标的GT，从而变相增大目标

&emsp;&emsp;6. Focal loss，通过降低正样本的权重来变相提高负样本的权重，这里负样本就是难检样本，即小目标

### 4、回归框损失
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
$v=\frac{4}{\pi ^{2}}(arctan\frac{w^{gt}}{h^{gt}}-arctan\frac{w^{p}}{h^{p}})^{2}$

&emsp;&emsp;CIoU考虑了三个重要的几何因素：重叠面积、中心点距离、长宽比
