# 121. 买卖股票的最佳时机
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
# 难度：简单
#
# 给定一个数组 prices，它的第 i 个元素 prices[i] 表示一支股票第 i 天的价格。
# 只能选择某一天买入，并选择未来某一天卖出，返回最大利润。
#
# 示例：
# 输入：prices = [7,1,5,3,6,4]  输出：5
# 输入：prices = [7,6,4,3,1]    输出：0

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_price 表示当前天之前见过的最低买入价。
        min_price = float("inf")
        ans = 0

        for price in prices:
            # 如果今天价格更低，就把今天作为更优买入日。
            min_price = min(min_price, price)
            # 如果今天卖出，利润就是 price - min_price。
            ans = max(ans, price - min_price)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # 5
    print(s.maxProfit([7, 6, 4, 3, 1]))     # 0

