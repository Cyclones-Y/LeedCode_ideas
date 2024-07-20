"""给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，
并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。"""

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

insert_pos = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[insert_pos] = nums[i]
        insert_pos += 1
print(nums[:insert_pos])

"""
算法解释：“双指针”
原地删除数字，从数组中循环查看是否有值为val的num，如果不为val则将数字往前移

"""