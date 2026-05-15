# 746. 使用最小花费爬楼梯
# https://leetcode.cn/problems/min-cost-climbing-stairs/
# 难度：简单
#
# 给你一个整数数组 cost，其中 cost[i] 是从第 i 个台阶向上爬需要支付的费用。
# 每次可以爬 1 或 2 个台阶。可以从下标 0 或下标 1 开始。
# 返回到达楼顶的最低花费。
#
# 示例：
# 输入：cost = [10,15,20]              输出：15
# 输入：cost = [1,100,1,1,1,100,1,1,100,1]  输出：6
#
# 和 70. 爬楼梯关系：
# 70 求“方案数”，转移是相加；
# 746 求“最小代价”，转移是取 min。

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] 表示到达第 i 阶楼梯顶部的最低花费。
        # 这里的楼顶是第 len(cost) 阶，不对应 cost 中的实际台阶。
        n = len(cost)
        dp = [0] * (n + 1)

        # 可以从第 0 阶或第 1 阶开始，所以到达这两个位置本身不需要花费。
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n + 1):
            # 到达 i 可以从 i - 1 爬一步，支付 cost[i - 1]；
            # 也可以从 i - 2 爬两步，支付 cost[i - 2]。
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[n]

    def minCostClimbingStairsOptimized(self, cost: List[int]) -> int:
        # 空间压缩：prev2 表示 dp[i - 2]，prev1 表示 dp[i - 1]。
        prev2 = 0
        prev1 = 0

        for i in range(2, len(cost) + 1):
            curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            prev2, prev1 = prev1, curr

        return prev1


if __name__ == "__main__":
    s = Solution()
    print(s.minCostClimbingStairs([10, 15, 20]))  # 15
    print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6
    print(s.minCostClimbingStairsOptimized([10, 15, 20]))  # 15

