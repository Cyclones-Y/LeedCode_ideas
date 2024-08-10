"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
示例 1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例 2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：
输入：digits = [0]
输出：[1]

"""
from typing import List

""" 
未做完
"""
class Solution:
    def plusOne(self, digits: List[int]) :
        # 倒序，检查最后一名元素是否需要进位
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        # 如果digits在循环中没有return出去，则代表digits中全为需要进位的。
        return [1] + digits


if __name__ == '__main__':
    digits = [9, 9, 9, 9, 9]
    result = Solution()
    results = result.plusOne(digits)
    print(results)