# 437. 路径总和 III
# https://leetcode.cn/problems/path-sum-iii/
# 难度：中等
#
# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，
# 求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的。
#
# 示例：
# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8  输出：3

from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # prefix = defaultdict(int)
        # prefix[0] = 1

        # def dfs(node: Optional[TreeNode], curr: int) -> int:
        #     if not node:
        #         return 0

        #     curr += node.val
        #     count = prefix[curr - targetSum]
        #     prefix[curr] += 1

        #     count += dfs(node.left, curr)
        #     count += dfs(node.right, curr)

        #     prefix[curr] -= 1
        #     return count

        # return dfs(root, 0)
        prefix = defaultdict(int)
        prefix[0] = 1
        def dfs(node, curr):
            if not node:
                return 0
            curr += node.val
            count = prefix[curr-targetSum]
            prefix[curr] += 1
            count += dfs(node.left, curr)
            count += dfs(node.right, curr)
            prefix[curr] -= 1
            return count
        return dfs(root, 0)


def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


if __name__ == "__main__":
    s = Solution()
    root = build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    print(s.pathSum(root, 8))  # 3
