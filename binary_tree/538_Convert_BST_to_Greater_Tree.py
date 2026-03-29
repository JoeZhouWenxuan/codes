# 538. 把二叉搜索树转换为累加树
# https://leetcode.cn/problems/convert-bst-to-greater-tree/
# 难度：中等
#
# 给出二叉搜索树的根节点，该树的节点值各不相同，请你将其转换为累加树，
# 使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
#
# 示例：
# 输入：root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal total
            if not node:
                return
            dfs(node.right)
            total += node.val
            node.val = total
            dfs(node.left)

        dfs(root)
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
    print(
        level_order_values(
            s.convertBST(
                build_tree([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
            )
        )
    )  # [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]
