## 直线检测

- 霍夫变换检测直线，Hough-line

&emsp;&emsp;最大的缺点就是需要根据图片去调节参数

- HoughP_line检测

&emsp;&emsp;Hough_line的改进

- LSD直线检测算法

&emsp;&emsp;优于Hough算法，一般来说，要检测图中的直线，最基本的思想就是检测图像中梯度变化，较大的像素点集，LSD算法也正是利用梯度信息和行列线(level-line)来进行直线检测的

- FLD

&emsp;&emsp;使用直线特征来代替原始的SURF点特征进行建筑物识别。与点特征相比，先特征具有更容易发现和更好的鲁棒性，线特征基本上不会受到光照、遮挡、视角变化的影响

- EDlines

&emsp;&emsp;快速无参数的线段检测器

- LSWMS

&emsp;&emsp;精确且实时

- Cannylines

- MCMLSD

- LSM
