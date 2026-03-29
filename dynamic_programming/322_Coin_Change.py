# 322. 零钱兑换
# https://leetcode.cn/problems/coin-change/
# 难度：中等
#
# 给你一个整数数组 coins，表示不同面额的硬币；以及一个整数 amount，表示总金额。
# 计算并返回可以凑成总金额所需的最少硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#
# 示例：
# 输入：coins = [1,2,5], amount = 11    输出：3
# 输入：coins = [2], amount = 3         输出：-1

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for coin in coins:
            for total in range(coin, amount+1):
                dp[total] = min(dp[total], dp[total-coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
    
if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))  # 3
    print(s.coinChange([2], 3))         # -1
