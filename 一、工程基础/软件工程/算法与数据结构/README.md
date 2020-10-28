# 算法与数据结构
## 排序算法
&emsp;&emsp;[代码实现点我](sort_algorithm.ipynb)

&emsp;&emsp;排序算法一览：
<div align=center><img width="800" height="500" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/Sorting_Algorithm_Table.png"/></div>

### A、比较类排序
通过比较来决定元素间的相对次序，由于其时间复杂度不能突破O(nlogn)，因此也称为非线性时间比较类排序
1、交换排序
- 冒泡排序

&emsp;&emsp;算法步骤：

&emsp;&emsp;①、比较每一对相邻的元素，从开头到结尾，如果第一个比第二个大，就交换它们两个，这样在最后的元素是最大的数

&emsp;&emsp;②、除了最后面的已经排序好的，对剩下的元素继续进行①步骤，直到排序完成
<div align=center><img width="500" height="200" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/Bubble_Sort.gif"/></div>
- 快速排序

&emsp;&emsp;快速排序是冒泡排序的进阶，采用了分治法的思想，将数列分成两个子数列，然后对子数列重复分治法的思想，直至完成排序
<div align=center><img width="250" height="200" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/Quick_Sort0.png"/></div>

&emsp;&emsp;算法步骤：

&emsp;&emsp;①、从数列中挑选一个基准(pivot)

&emsp;&emsp;②、重新排列数列，小于基准的元素放在左边，大于的放在右边，基准位于两个子数列的中间

&emsp;&emsp;③、递归的对两个子数列进行①、②步骤
<div align=center><img width="250" height="300" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/Quick_Sort1.png"/></div>

2、插入排序
- 插入排序

&emsp;&emsp;工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入

&emsp;&emsp;算法步骤：

&emsp;&emsp;①、从一个元素开始，该元素可以认为已被排序

&emsp;&emsp;②、取出下一个元素，在已排序的元素序列中从后向前扫描

&emsp;&emsp;③、如果该元素(已排序)大于新元素，将该元素移到下一位置

&emsp;&emsp;④、重复步骤③，直至找到已排序的元素小于或等于新元素的位置

&emsp;&emsp;⑤、将新元素插入到该位置后，重复步骤②~⑤
<div align=center><img width="500" height="200" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/Insertion_Sort.gif"/></div>

- 希尔排序

3、选择排序
- 选择排序

&emsp;&emsp;表现最稳定的排序算法之一，因为无论什么数据进去都是$O(n^{2})$的时间复杂度，所以用到它的时候，数据规模越小越好

&emsp;&emsp;算法步骤：

&emsp;&emsp;①、首先在给定序列中找到最小的值，放在起始位置

&emsp;&emsp;②、在剩下的序列中找到最小的值，放在已排序序列的末尾

&emsp;&emsp;③、重复②步骤，直至序列顺序排列

- 堆排序

4、归并排序
- 归并排序

&emsp;&emsp;归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法的一个非常典型的应用，将已有序的子序列合并，得到完全有序的序列，即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2路归并

&emsp;&emsp;归并排序是一种稳定的排序方法，和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是O(nlogn)的时间复杂度，代价是需要额外的内存空间

&emsp;&emsp;算法步骤：

&emsp;&emsp;①、把长度为n的输入序列分成两个长度为n/2的子序列

&emsp;&emsp;②、对这两个子序列分别采用归并排序

&emsp;&emsp;③、将两个排序好的子序列合并成一个最终的排序序列


### B、非比较排序

&emsp;&emsp;不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时间下界，以线性时间运行，因此也称为线性时间非比较类排序

- 计数排序

&emsp;&emsp;计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数

&emsp;&emsp;算法步骤：

&emsp;&emsp;①、找出待排序的最大的值，然后创建一个覆盖待排序数组数值的统计数组

&emsp;&emsp;②、遍历待排序数组，将各值出现的次数记录下来

&emsp;&emsp;③、按照统计数组，将待排序数组进行重排
<div align=center><img width="500" height="200" src="https://github.com/ethan-sui/AI-algorithm-engineer-knowledge/blob/main/image/Count_Sort.gif"/></div>

- 桶排序
- 基数排序
