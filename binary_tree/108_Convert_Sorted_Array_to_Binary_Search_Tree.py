# 108. 将有序数组转换为二叉搜索树
# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
# 难度：简单
#
# 给你一个整数数组 nums ，其中元素已经按升序排列，
# 请你将其转换为一棵平衡二叉搜索树。
#
# 示例：
# 输入：nums = [-10,-3,0,5,9]
# 输出：一棵高度平衡 BST

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, len(nums) - 1)


def inorder_values(root):
    res = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    dfs(root)
    return res


if __name__ == "__main__":
    s = Solution()
    root = s.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(inorder_values(root))  # [-10, -3, 0, 5, 9]
