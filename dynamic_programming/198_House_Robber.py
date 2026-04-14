# 198. 打家劫舍
# https://leetcode.cn/problems/house-robber/
# 难度：中等
#
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
# 相邻的房屋装有相互连通的防盗系统。计算你不触动警报装置的情况下，能够偷窃到的最高金额。
#
# 示例：
# 输入：nums = [1,2,3,1]    输出：4
# 输入：nums = [2,7,9,3,1]  输出：12

from typing import List


class Solution:
    def rob_dp(self, nums: List[int]) -> int:
        # 原始 DP 写法：
        # dp[i] 表示“偷到第 i 间房为止，能偷到的最大金额”。
        # 对于第 i 间房，只有两种选择：
        # 1. 不偷它，答案就是 dp[i - 1]
        # 2. 偷它，答案就是 dp[i - 2] + nums[i]
        # 所以转移方程为：
        # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        # 滚动变量写法，本质上是把 dp 数组压缩成两个变量。
        # a 表示“前前一家为止的最优解”，对应旧的 dp[i - 2]
        # b 表示“前一家为止的最优解”，对应旧的 dp[i - 1]
        # 当前处理到 num 时：
        # - 不偷当前这家：收益是 b
        # - 偷当前这家：收益是 a + num
        # 更新后新的 b 就是“处理到当前房子为止的最优解”。
        # a, b = 0, 0
        # for num in nums:
        #     a, b = b, max(b, a + num)
        # return b
        a, b = nums[0], max(nums[: 2])
        for num in nums[2: ]:
            a, b = b, max(b, a+num)
        return b
if __name__ == "__main__":
    s = Solution()
    print(s.rob_dp([1, 2, 3, 1]))     # 4
    print(s.rob_dp([2, 7, 9, 3, 1]))  # 12
    print(s.rob([1, 2, 3, 1]))        # 4
    print(s.rob([2, 7, 9, 3, 1]))     # 12
