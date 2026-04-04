# 101. 对称二叉树
# https://leetcode.cn/problems/symmetric-tree/
# 难度：简单
#
# 给你一个二叉树的根节点 root ，检查它是否轴对称。
#
# 示例：
# 输入：root = [1,2,2,3,4,4,3]          输出：True
# 输入：root = [1,2,2,null,3,null,3]    输出：False

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # def check(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        #     if not left and not right:
        #         return True
        #     if not left or not right or left.val != right.val:
        #         return False
        #     return check(left.left, right.right) and check(left.right, right.left)

        # return check(root.left, root.right) if root else True

        def check(left, right):
            if left is None and right is None:
                return True
            if not left or not right or left.val != right.val:
                return False
            return check(left.left, right.right) and check(left.right, right.left)
        return check(root.left, root.right) if root else True

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
    print(s.isSymmetric(build_tree([1, 2, 2, 3, 4, 4, 3])))          # True
    print(s.isSymmetric(build_tree([1, 2, 2, None, 3, None, 3])))    # False
