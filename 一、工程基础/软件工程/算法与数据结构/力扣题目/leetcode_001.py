# 1、两数之和
# 一、暴力求解，两层循环，时间复杂度O(n^2),空间复杂度O(1)
def twoSum1(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
# 二、哈希表来做，检查target-num是否在哈希表中，这样就可以将O(n)降为O(1)，所以总时间复杂度为O(n),空间时间复杂度O(n)
def twoSum2(nums, target):
    hashTable = {}
    for i, num in enumerate(nums):
        if target-num in hashTable:
            return [hashTable[target-num], i]
        hashTable[num] = i

nums = [2, 7, 11, 15]
targets = 9
print(twoSum2(nums, targets))
