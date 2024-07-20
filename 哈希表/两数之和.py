"""两数之和
将 target 与循环中的一个数 num 作差，得到diff ,在表中查看是否存在已有的diff数，如果有则返回索引值
如果没有就将num 存到表里 然后做下一次循环
"""
def twonums(nums, target):
    num_dict = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in num_dict:
            return [num_dict[diff], index]
        num_dict[num] = index
    return []


nums = [1, 2, 3, 4, 6, 8]
target = 6
print(twonums(nums, target))
