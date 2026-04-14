# 494. 目标和
# https://leetcode.cn/problems/target-sum/
# 难度：中等
#
# 给你一个非负整数数组 nums 和一个整数 target。
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个表达式。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同表达式的数目。
#
# 示例：
# 输入：nums = [1,1,1,1,1], target = 3    输出：5
# 输入：nums = [1], target = 1            输出：1

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # total = sum(nums)
        # if abs(target) > total or (total + target) % 2 != 0:
        #     return 0

        # subset_sum = (total + target) // 2
        # dp = [0] * (subset_sum + 1)
        # dp[0] = 1

        # for num in nums:
        #     for j in range(subset_sum, num - 1, -1):
        #         dp[j] += dp[j - num]

        # return dp[subset_sum]

        # total = sum(nums)
        # if total < abs(target) or (total + target) % 2 != 0:
        #     return 0
        # P = (total + target) // 2
        # # dp[j] 恰好凑出和j的方案数
        # dp = [0] * (P+1)
        # dp[0] = 1
        # for num in nums:
        #     for j in range(P, num - 1, -1):
        #         dp[j] += dp[j - num]
        # return dp[-1]
        total = sum(nums)
        if total < abs(target) or (total + target) % 2 != 0:
            return 0
        P = (total + target) // 2
        dp = [0] * (P + 1)
        dp[0] = 1
        for num in nums:
            for j in range(P, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))  # 5
    print(s.findTargetSumWays([1], 1))              # 1
