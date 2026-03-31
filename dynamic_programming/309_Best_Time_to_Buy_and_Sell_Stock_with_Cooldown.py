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
        '''
        2. 三个状态分别是什么意思
        hold
        表示：
        今天结束时，手里持有一支股票时的最大利润
        也就是说：
        你可能之前就持有
        也可能今天刚买入

        sold
        表示：
        今天结束时，刚刚卖出股票时的最大利润
        注意这是“今天卖了”。
        它对应的是冷冻期的来源。

        rest
        表示：
        今天结束时，手里没有股票，并且今天不是刚卖出时的最大利润
        也就是普通休息状态。
        '''
        hold = -prices[0]
        sold = 0
        rest = 0

        for price in prices[1:]:
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest
            '''
            情况 1：昨天就有，今天什么都不做
            prev_hold
            情况 2：昨天处于休息状态，今天买入
            prev_rest - price
            为什么不能从 prev_sold 买？
            因为昨天刚卖，今天处于冷冻期，不能买。

            所以：
            hold = max(prev_hold, prev_rest - price)
            '''
            hold = max(prev_hold, prev_rest - price)
            '''
            sold = prev_hold + price
            今天结束时刚卖出股票，只能来自一种情况：
            昨天手里有股票
            今天把它卖掉
            所以：
            sold = prev_hold + price
            '''
            sold = prev_hold + price
            '''
            rest = max(prev_rest, prev_sold)
            今天结束时处于休息状态，也有两种可能：

            情况 1：昨天就休息，今天继续休息
            prev_rest
            情况 2：昨天刚卖出，今天进入冷冻/休息状态
            prev_sold
            所以：
            rest = max(prev_rest, prev_sold)
            '''
            rest = max(prev_rest, prev_sold)

        return max(sold, rest)


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1, 2, 3, 0, 2]))  # 3
    print(s.maxProfit([1]))              # 0
