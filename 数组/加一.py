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
        numbers = int(''.join([str(i) for i in digits]))
        print(numbers)
        add_num = numbers + 1
        print(add_num)
        if len(str(add_num)) != len(str(numbers)):
            return_list = [int(i) for i in str(add_num)]
            return return_list


if __name__ == '__main__':
    digits = [4, 3, 2, 9]
    result = Solution()
    results = result.plusOne(digits)
    print(results)
