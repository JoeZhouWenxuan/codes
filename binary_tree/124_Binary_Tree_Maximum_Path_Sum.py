# 124. 二叉树中的最大路径和
# https://leetcode.cn/problems/binary-tree-maximum-path-sum/
# 难度：困难
#
# 路径被定义为一条从树中任意节点出发，沿父子节点连接，达到任意节点的序列。
# 同一个节点在一条路径序列中至多出现一次。该路径至少包含一个节点，且不一定经过根节点。
#
# 示例：
# 输入：root = [1,2,3]                    输出：6
# 输入：root = [-10,9,20,null,null,15,7]  输出：42

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # ans = float("-inf")

        # def dfs(node: Optional[TreeNode]) -> int:
        #     nonlocal ans
        #     if not node:
        #         return 0

        #     left = max(dfs(node.left), 0)
        #     right = max(dfs(node.right), 0)
        #     ans = max(ans, node.val + left + right)
        #     return node.val + max(left, right)

        # dfs(root)
        # return ans

        ans = float('-inf')
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            left_value = max(0, dfs(node.left))
            right_value = max(0, dfs(node.right))
            ans = max(ans, node.val + left_value + right_value)
            return node.val + max(left_value, right_value)

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
    print(s.maxPathSum(build_tree([1, 2, 3])))                         # 6
    print(s.maxPathSum(build_tree([-10, 9, 20, None, None, 15, 7])))   # 42
