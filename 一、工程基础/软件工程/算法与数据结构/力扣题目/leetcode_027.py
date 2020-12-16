# 27、移除元素
# 一、双指针法，设置快慢指针，当快指针指向元素等于删除元素时，快指针快走一步，
#    慢指针不走；否则，快慢指针同时走一步，并把快指针的元素值赋给慢指针，这样
#    慢指针走过的元素就是删除掉指定元素的数组，时间复杂度O(n)，空间复杂度O(1)
def removeElement0(nums, val):
    if len(nums) == 0:
        return 0
    left = 0
    right = 0
    while right < len(nums):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1
            right += 1
        else:
            right += 1
    return left

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(removeElement0(nums, val))