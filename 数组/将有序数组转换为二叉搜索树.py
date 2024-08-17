"""
二叉树

若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树。

"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        # 中间值
        mid = len(nums) // 2
        # 根节点
        root = TreeNode(nums[mid])

        # 递归构建左子树
        root.left = Solution.sortedArrayToBST(self, nums[: mid])
        # 递归构建右子树
        root.right = Solution.sortedArrayToBST(self, nums[mid + 1:])

        return root


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    instance = Solution()
    result = instance.sortedArrayToBST(nums)
    print(result)