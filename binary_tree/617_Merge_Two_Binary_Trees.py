# 617. 合并二叉树
# https://leetcode.cn/problems/merge-two-binary-trees/
# 难度：简单
#
# 给你两棵二叉树：root1 和 root2。
# 想象一下，当你将其中一棵覆盖到另一棵之上时，两个二叉树的一些节点便会重叠。
# 你需要将这两棵树合并成一棵新二叉树。合并的规则是：
# 如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；
# 否则，不为 null 的节点将直接作为新二叉树的节点。
#
# 示例：
# 输入：root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]    输出：[3,4,5,5,4,null,7]
# 输入：root1 = [1], root2 = [1,2]                          输出：[2,2]

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        # if not root1:
        #     return root2
        # if not root2:
        #     return root1

        # root1.val += root2.val
        # root1.left = self.mergeTrees(root1.left, root2.left)
        # root1.right = self.mergeTrees(root1.right, root2.right)
        # return root1
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1


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
            s.mergeTrees(
                build_tree([1, 3, 2, 5]),
                build_tree([2, 1, 3, None, 4, None, 7]),
            )
        )
    )  # [3, 4, 5, 5, 4, None, 7]
    print(level_order_values(s.mergeTrees(build_tree([1]), build_tree([1, 2]))))  # [2, 2]
