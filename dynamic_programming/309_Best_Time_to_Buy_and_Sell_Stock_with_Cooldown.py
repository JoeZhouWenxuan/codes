# 309. 买卖股票的最佳时机含冷冻期
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# 难度：中等
#
# 给定一个整数数组 prices，其中第 prices[i] 表示第 i 天的股票价格。
# 设计一个算法计算出最大利润。你可以多次买卖，但卖出股票后无法在第二天买入股票。
#
# 示例：
# 输入：prices = [1,2,3,0,2]    输出：3
# 输入：prices = [1]            输出：0

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        sold = 0
        rest = 0

        for price in prices[1:]:
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            hold = max(prev_hold, prev_rest - price)
            sold = prev_hold + price
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1, 2, 3, 0, 2]))  # 3
    print(s.maxProfit([1]))              # 0
