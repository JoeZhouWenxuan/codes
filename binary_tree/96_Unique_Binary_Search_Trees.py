# 96. 不同的二叉搜索树
# https://leetcode.cn/problems/unique-binary-search-trees/
# 难度：中等
#
# 给你一个整数 n，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的二叉搜索树有多少种。
#
# 示例：
# 输入：n = 3    输出：5
# 输入：n = 1    输出：1


class Solution:
    def numTrees(self, n: int) -> int:
        # dp = [0] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1

        # for nodes in range(2, n + 1):
        #     for root in range(1, nodes + 1):
        #         dp[nodes] += dp[root - 1] * dp[nodes - root]

        # return dp[n]
        dp = [0] * (n + 1) # 空节点为空树
        dp[0] = dp[1] = 1

        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                dp[root] += dp[root-1] * dp[nodes-root]
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(3))  # 5
    print(s.numTrees(1))  # 1
