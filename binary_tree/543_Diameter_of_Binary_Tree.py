# 543. 二叉树的直径
# https://leetcode.cn/problems/diameter-of-binary-tree/
# 难度：简单
#
# 给你一棵二叉树的根节点，返回该树的 直径 。
# 二叉树的直径是指树中任意两个节点之间最长路径的长度，这条路径可能不经过根节点。
#
# 示例：
# 输入：root = [1,2,3,4,5]  输出：3
# 输入：root = [1,2]        输出：1

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # ans = 0

        # def depth(node: Optional[TreeNode]) -> int:
        #     nonlocal ans
        #     if not node:
        #         return 0
        #     left = depth(node.left)
        #     right = depth(node.right)
        #     ans = max(ans, left + right)
        #     return max(left, right) + 1

        # depth(root)
        # return ans
        ans = 0
        def depth(node):
            nonlocal ans
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            ans = max(ans, left+right)
            return max(left, right) + 1
        depth(root)
        return ans


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
    print(s.diameterOfBinaryTree(build_tree([1, 2, 3, 4, 5])))  # 3
    print(s.diameterOfBinaryTree(build_tree([1, 2])))           # 1
