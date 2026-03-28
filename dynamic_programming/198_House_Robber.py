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
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0

        for num in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + num)

        return prev1


if __name__ == "__main__":
    s = Solution()
    print(s.rob([1, 2, 3, 1]))     # 4
    print(s.rob([2, 7, 9, 3, 1]))  # 12
