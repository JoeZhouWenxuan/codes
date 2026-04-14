# 236. 二叉树的最近公共祖先
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
# 难度：中等
#
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 示例：
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1  输出：3
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4  输出：5

from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self,
        root: Optional[TreeNode],
        p: Optional[TreeNode],
        q: Optional[TreeNode],
    ) -> Optional[TreeNode]:
        # if not root or root == p or root == q:
        #     return root

        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if left and right:
        #     return root
        # return left or right

        if not root or root is p or root is q: # 我已经在当前子树里找到一个目标节点了，你上层自己决定怎么用它
            return root
        left = self.lowestCommonAncestor(root.left, p, q) # 去左子树看看有没有找到 p / q / 最近公共祖先
        right = self.lowestCommonAncestor(root.right, p, q) # 右子树看看有没有找到 p / q / 最近公共祖先
        if left and right:  # 两个都不为空，p和q分别在当前节点左右子树，则root是最近
            return root
        
        return left or right
        

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


def find_node(root, target):
    if not root:
        return None
    if root.val == target:
        return root
    return find_node(root.left, target) or find_node(root.right, target)


if __name__ == "__main__":
    s = Solution()
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print(s.lowestCommonAncestor(root, find_node(root, 5), find_node(root, 1)).val)  # 3
    print(s.lowestCommonAncestor(root, find_node(root, 5), find_node(root, 4)).val)  # 5
