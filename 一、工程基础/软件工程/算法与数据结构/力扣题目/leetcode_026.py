# 2、删除排序数组中的重复项
# 一、双指针法，设置快慢指针，当快慢指针指向元素一样时，快指针快走一步，
#    当快慢指针指向元素不同时，同时走一步，并把快指针的元素值赋给慢指针，
#    这样，慢指针走过的元素就是不重复的元素
#    时间复杂度O(n)，空间复杂度O(1)
def removeDuplicates0(arr):
    if len(arr) == 0:
        return 0
    left = 0
    right = 1
    while right < len(arr):
        if arr[right] != arr[left]:
            left += 1
            arr[left] = arr[right]
            right += 1
        else:
            right += 1
    return left + 1

nums = [1, 1, 2]
print(removeDuplicates0(nums))