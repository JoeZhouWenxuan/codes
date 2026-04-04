# 121. 买卖股票的最佳时机
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
# 难度：简单
#
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。
# 设计一个算法来计算你所能获取的最大利润。
#
# 示例：
# 输入：prices = [7,1,5,3,6,4]    输出：5

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        ans = 0

        for price in prices:
            min_price = min(min_price, price)
            ans = max(ans, price - min_price)

        return ans

    def maxProfit(self, prices: List[int]) -> int:
        price_min = float('inf')
        ans = 0
        for p in prices:
            price_min = min(p, price_min)
            ans = max(ans, p - price_min)
        return ans
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
    print(s.maxProfit([7, 6, 4, 3, 1]))     # 0
