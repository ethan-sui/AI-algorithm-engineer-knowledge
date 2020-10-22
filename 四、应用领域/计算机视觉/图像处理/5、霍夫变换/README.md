## 霍夫变换

&emsp;&emsp;可以检测直线

&emsp;&emsp;①、先将图像进行二值化，然后Canny进行边缘检测；

&emsp;&emsp;②、霍夫变化
<div align=center><img width="500" height="200" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/Hough00.jpg"/></div>
&emsp;&emsp;即一组$(r,\theta)$便可确定一条直线，所以我们就是要找这些潜在直线对应的$(r,\theta)$，

&emsp;&emsp;霍夫变换找直线的过程其实就是一个投票的过程，最后投票高的$(r,\theta)$便是所需直线，对图a进行遍历遇到背景就跳过，遇到边缘代入x,y到公式求得$r$，$\theta$进行投票
<div align=center><img width="500" height="200" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/Hough01.jpg"/></div>
