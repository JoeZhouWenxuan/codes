# 416. 分割等和子集
# https://leetcode.cn/problems/partition-equal-subset-sum/
# 难度：中等
#
# 给你一个只包含正整数的非空数组 nums，判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
# 示例：
# 输入：nums = [1,5,11,5]    输出：True
# 输入：nums = [1,2,3,5]     输出：False

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        # dp[i] 是否可以恰好凑出和 i
        dp = [True] + [False] * target

        for num in nums:
            for total in range(target, num - 1, -1):
                dp[total] = dp[total] or dp[total-num]

        return dp[-1]
        
if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1, 5, 11, 5]))  # True
    print(s.canPartition([1, 2, 3, 5]))   # False
