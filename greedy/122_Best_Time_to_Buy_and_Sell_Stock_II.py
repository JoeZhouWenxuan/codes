# 122. 买卖股票的最佳时机 II
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/
# 难度：中等
#
# 给你一个整数数组 prices，其中 prices[i] 表示某支股票第 i 天的价格。
# 每天可以买入或卖出股票，但同一时间最多只能持有一股股票。
# 可以完成任意多次交易，返回能获得的最大利润。
#
# 示例：
# 输入：prices = [7,1,5,3,6,4]  输出：7
# 输入：prices = [1,2,3,4,5]    输出：4
# 输入：prices = [7,6,4,3,1]    输出：0

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        for i in range(1, len(prices)):
            # 只要今天价格比昨天高，就把这段上涨收益加入答案。
            # 连续上涨可以拆成每天买卖，收益等价于最低点买入、最高点卖出。
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 7
    print(s.maxProfit([1, 2, 3, 4, 5]))     # 4
    print(s.maxProfit([7, 6, 4, 3, 1]))     # 0

