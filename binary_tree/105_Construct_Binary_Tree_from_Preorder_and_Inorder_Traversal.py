# 105. 从前序与中序遍历序列构造二叉树
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 难度：中等
#
# 给定两个整数数组 preorder 和 inorder ，
# 其中 preorder 是二叉树的前序遍历，inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
#
# 示例：
# 输入：preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出：对应的二叉树根节点

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder) -> Optional[TreeNode]:
        index = {value: i for i, value in enumerate(inorder)}

        def dfs(pre_l: int, pre_r: int, in_l: int, in_r: int) -> Optional[TreeNode]:
            if pre_l > pre_r:
                return None

            root_val = preorder[pre_l]
            root = TreeNode(root_val)
            pivot = index[root_val]
            left_size = pivot - in_l

            root.left = dfs(pre_l + 1, pre_l + left_size, in_l, pivot - 1)
            root.right = dfs(pre_l + left_size + 1, pre_r, pivot + 1, in_r)
            return root

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)


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
    root = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(level_order_values(root))  # [3, 9, 20, None, None, 15, 7]
