# 230. 二叉搜索树中第 K 小的元素
# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/
# 难度：中等
#
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，
# 请你设计一个算法查找其中第 k 小的元素。
#
# 示例：
# 输入：root = [3,1,4,null,2], k = 1         输出：1
# 输入：root = [5,3,6,2,4,null,null,1], k=3  输出：3

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        raise ValueError("k 超出节点数量范围")


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
    print(s.kthSmallest(build_tree([3, 1, 4, None, 2]), 1))                 # 1
    print(s.kthSmallest(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3))     # 3
