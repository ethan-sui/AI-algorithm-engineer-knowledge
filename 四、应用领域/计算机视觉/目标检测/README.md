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
