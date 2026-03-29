# 337. 打家劫舍 III
# https://leetcode.cn/problems/house-robber-iii/
# 难度：中等
#
# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root。
# 除了 root 之外，每栋房子有且只有一个“父“房子与之相连。
# 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
# 计算在不触动警报的情况下，小偷能够盗取的最高金额。
#
# 示例：
# 输入：root = [3,2,3,null,3,null,1]    输出：7
# 输入：root = [3,4,5,1,3,null,1]       输出：9

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0, 0

            left = dfs(node.left)
            right = dfs(node.right)

            rob_current = node.val + left[1] + right[1]
            skip_current = max(left) + max(right)
            return rob_current, skip_current

        return max(dfs(root))


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
    print(s.rob(build_tree([3, 2, 3, None, 3, None, 1])))  # 7
    print(s.rob(build_tree([3, 4, 5, 1, 3, None, 1])))     # 9
