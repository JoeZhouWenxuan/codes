# 114. 二叉树展开为链表
# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
# 难度：中等
#
# 给你二叉树的根结点 root ，请你将它展开为一个单链表：
#   1. 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点
#   2. left 子指针始终为 null
#   3. 展开后的单链表应该与二叉树前序遍历顺序相同
#
# 示例：
# 输入：root = [1,2,5,3,4,null,6]
# 输出：1 -> 2 -> 3 -> 4 -> 5 -> 6

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
        #     if not node:
        #         return None

        #     left_tail = dfs(node.left)
        #     right_tail = dfs(node.right)

        #     if node.left:
        #         tail = left_tail
        #         tail.right = node.right
        #         node.right = node.left
        #         node.left = None

        #     return right_tail or left_tail or node

        # dfs(root)
        def dfs(node):
            if not node:
                return None
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)
            if left_tail:
                tail = left_tail
                tail.right = node.right
                node.right = node.left
                node.left = None
            return left_tail or right_tail or node
        dfs(root)
        


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


def right_chain_values(root):
    res = []
    while root:
        res.append(root.val)
        root = root.right
    return res


if __name__ == "__main__":
    s = Solution()
    root = build_tree([1, 2, 5, 3, 4, None, 6])
    s.flatten(root)
    print(right_chain_values(root))  # [1, 2, 3, 4, 5, 6]
