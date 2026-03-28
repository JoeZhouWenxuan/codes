# 104. 二叉树的最大深度
# https://leetcode.cn/problems/maximum-depth-of-binary-tree/
# 难度：简单
#
# 给定一个二叉树 root ，返回其最大深度。
#
# 示例：
# 输入：root = [3,9,20,null,null,15,7]  输出：3
# 输入：root = [1,null,2]               输出：2

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


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
    print(s.maxDepth(build_tree([3, 9, 20, None, None, 15, 7])))  # 3
    print(s.maxDepth(build_tree([1, None, 2])))                   # 2
