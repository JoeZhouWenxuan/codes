# 53. 最大子数组和
# https://leetcode.cn/problems/maximum-subarray/
# 难度：中等
#
# 给你一个整数数组 nums，请你找出一个具有最大和的连续子数组，返回其最大和。
#
# 示例：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]  输出：6
# 输入：nums = [1]                       输出：1

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # current 表示以当前元素结尾的最大连续子数组和。
        # best 表示目前见过的最大连续子数组和。
        current = best = nums[0]

        for num in nums[1:]:
            # 如果 current + num 不如 num，说明前面的连续和拖后腿，从当前 num 重新开始。
            current = max(num, current + num)
            best = max(best, current)

        return best


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(s.maxSubArray([1]))                               # 1

