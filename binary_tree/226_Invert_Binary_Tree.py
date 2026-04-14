# 226. 翻转二叉树
# https://leetcode.cn/problems/invert-binary-tree/
# 难度：简单
#
# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
#
# 示例：
# 输入：root = [4,2,7,1,3,6,9]  输出：[4,7,2,9,6,3,1]
# 输入：root = [2,1,3]          输出：[2,3,1]

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if not root:
    #         return None
    #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    #     return root
        if not root:
            return None
        root.right, root.left = self.invertTree(root.left),  self.invertTree(root.right)
        return root


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


def level_order_values(root):
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    while res and res[-1] is None:
        res.pop()
    return res


if __name__ == "__main__":
    s = Solution()
    print(level_order_values(s.invertTree(build_tree([4, 2, 7, 1, 3, 6, 9]))))  # [4, 7, 2, 9, 6, 3, 1]
    print(level_order_values(s.invertTree(build_tree([2, 1, 3]))))               # [2, 3, 1]
