# 94. 二叉树的中序遍历
# https://leetcode.cn/problems/binary-tree-inorder-traversal/
# 难度：简单
#
# 给定一个二叉树的根节点 root ，返回它的中序遍历。
#
# 示例：
# 输入：root = [1,null,2,3]  输出：[1,3,2]
# 输入：root = []            输出：[]

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res


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
    print(s.inorderTraversal(build_tree([1, None, 2, 3])))  # [1, 3, 2]
    print(s.inorderTraversal(build_tree([])))                # []
