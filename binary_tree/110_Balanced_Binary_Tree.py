# 110. 平衡二叉树
# https://leetcode.cn/problems/balanced-binary-tree/
# 难度：简单
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 本题中，一棵高度平衡二叉树定义为：
# 一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1。
#
# 示例：
# 输入：root = [3,9,20,null,null,15,7]            输出：True
# 输入：root = [1,2,2,3,3,null,null,4,4]          输出：False

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # def height(node: Optional[TreeNode]) -> int:
        #     if not node:
        #         return 0

        #     left = height(node.left)
        #     if left == -1:
        #         return -1

        #     right = height(node.right)
        #     if right == -1:
        #         return -1

        #     if abs(left - right) > 1:
        #         return -1

        #     return max(left, right) + 1

        # return height(root) != -1

        def height(root):
            if not root:
                return 0
            
            left = height(root.left)
            if left == -1:
                return -1
            right = height(root.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1
        return height(root) != -1


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
    print(s.isBalanced(build_tree([3, 9, 20, None, None, 15, 7])))           # True
    print(s.isBalanced(build_tree([1, 2, 2, 3, 3, None, None, 4, 4])))       # False
