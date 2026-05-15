# 235. 二叉搜索树的最近公共祖先
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/
# 难度：中等
#
# 给定一个二叉搜索树，找到该树中两个指定节点 p 和 q 的最近公共祖先。
#
# 示例：
# 输入：root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8  输出：6
# 输入：root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4  输出：2
#
# 思路：利用二叉搜索树性质。
# 如果 p 和 q 都比当前节点小，最近公共祖先一定在左子树。
# 如果 p 和 q 都比当前节点大，最近公共祖先一定在右子树。
# 否则当前节点就是分叉点，也就是最近公共祖先。

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
        p: TreeNode,
        q: TreeNode,
    ) -> Optional[TreeNode]:
        cur = root
        low = min(p.val, q.val)
        high = max(p.val, q.val)

        while cur:
            # p 和 q 都在当前节点左侧，继续去左子树找。
            if high < cur.val:
                cur = cur.left
            # p 和 q 都在当前节点右侧，继续去右子树找。
            elif low > cur.val:
                cur = cur.right
            else:
                # 当前节点位于 [p, q] 之间，或者等于 p/q。
                # 说明 p 和 q 分布在当前节点两侧，或当前节点本身就是其中一个目标节点。
                return cur

        return None


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
    if target < root.val:
        return find_node(root.left, target)
    return find_node(root.right, target)


if __name__ == "__main__":
    s = Solution()
    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    print(s.lowestCommonAncestor(root, find_node(root, 2), find_node(root, 8)).val)  # 6
    print(s.lowestCommonAncestor(root, find_node(root, 2), find_node(root, 4)).val)  # 2

