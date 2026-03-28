# 300. 最长递增子序列
# https://leetcode.cn/problems/longest-increasing-subsequence/
# 难度：中等
#
# 给你一个整数数组 nums，找到其中最长严格递增子序列的长度。
#
# 示例：
# 输入：nums = [10,9,2,5,3,7,101,18]    输出：4
# 输入：nums = [0,1,0,3,2,3]            输出：4

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
    print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))            # 4
