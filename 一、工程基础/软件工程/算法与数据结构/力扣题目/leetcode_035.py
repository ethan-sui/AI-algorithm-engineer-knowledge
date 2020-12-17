# 35、搜索插入位置
# 一、暴力法，遍历所有的可能，寻找位置，时间复杂度O(n)，空间复杂度O(1)
def searchInsert0(nums, target):
    if target == nums[-1]:
        return len(nums)-1
    if target > nums[-1]:
        return len(nums)
    if target < nums[0]:
        return 0
    for i in range(len(nums)-1):
        if target == nums[i]:
            return i
        if nums[i] < target < nums[i+1]:
            return i+1
# 二、二分法，问题转化为寻找第一个大于等于target的元素下标
#     时间复杂度O(logn)，空间复杂度O(1)
def searchInsert1(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + int((right-left)/2)
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

nums = [1, 3, 5, 6]
target = 7
print(searchInsert1(nums, target))