## 目标检测的指标
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
