"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
"""
"""
示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2

示例 2:
输入: nums = [1,3,5,6], target = 2
输出: 1

示例 3:
输入: nums = [1,3,5,6], target = 7
输出: 4
"""
nums = [1, 3, 5, 6, 6, 7]
target = 5

left, right = 0, len(nums) - 1
while left <= right:
    mid = left + (right - left) // 2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
print(left)

"""
注释：使用二分查找
1. 不断缩小范围最后选择中间相等的值
2. 如果值不在数组内，那么该目标值的下标就在数组外面的左右两则，

:return: 范围目标值的下标
"""

# """
# 方法二
# """
# if target in nums :
#     print(nums.index(target))
# else:
#     nums.append(target)
#     nums.sort()
#     print(nums.index(target))
