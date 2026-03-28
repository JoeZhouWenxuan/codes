# 98. 验证二叉搜索树
# https://leetcode.cn/problems/validate-binary-search-tree/
# 难度：中等
#
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
# 示例：
# 输入：root = [2,1,3]                  输出：True
# 输入：root = [5,1,4,null,null,3,6]    输出：False

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float("-inf"), float("inf"))


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
    print(s.isValidBST(build_tree([2, 1, 3])))                 # True
    print(s.isValidBST(build_tree([5, 1, 4, None, None, 3, 6])))  # False
