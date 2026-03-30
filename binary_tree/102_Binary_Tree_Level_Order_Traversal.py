# 102. 二叉树的层序遍历
# https://leetcode.cn/problems/binary-tree-level-order-traversal/
# 难度：中等
#
# 给你二叉树的根节点 root ，返回其节点值的层序遍历。
#
# 示例：
# 输入：root = [3,9,20,null,null,15,7]  输出：[[3],[9,20],[15,7]]
# 输入：root = [1]                      输出：[[1]]

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []

        # res = []
        # queue = deque([root])
        # while queue:
        #     level = []
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         level.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     res.append(level)
        # return res
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)
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
    print(s.levelOrder(build_tree([3, 9, 20, None, None, 15, 7])))  # [[3], [9, 20], [15, 7]]
    print(s.levelOrder(build_tree([1])))                             # [[1]]
