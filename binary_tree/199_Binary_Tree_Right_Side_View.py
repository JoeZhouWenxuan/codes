# 199. 二叉树的右视图
# https://leetcode.cn/problems/binary-tree-right-side-view/
# 难度：中等
#
# 给定一个二叉树的根节点 root，想象自己站在它的右侧，
# 按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
# 示例：
# 输入：root = [1,2,3,null,5,null,4]  输出：[1,3,4]
# 输入：root = [1,null,3]             输出：[1,3]

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == size - 1:
                    res.append(node.val)
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
    print(s.rightSideView(build_tree([1, 2, 3, None, 5, None, 4])))  # [1, 3, 4]
    print(s.rightSideView(build_tree([1, None, 3])))                  # [1, 3]
