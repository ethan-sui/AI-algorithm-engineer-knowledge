## Anchor相关

&emsp;&emsp;anchor就是一系列的锚框，对于目标检测，不同的目标检测具有不同的宽高比，比如球类目标，可以用正方形框检测，而串或者筷子这种就可能需长方形矩形框来检测，所以有贴合于数据集的anchor会有较好的效果

&emsp;&emsp;anchor跟训练数据集有关，是通过K-means在数据集上聚类出来的，假设有如图所示数据集，我需要统计数据集中的高和宽以及宽高比，来进行聚类
<div align=center><img width="500" height="160" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/anchor01.PNG"/></div>
