# 581. 最短无序连续子数组
# https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/
# 难度：中等
#
# 给你一个整数数组 nums，你需要找出一个连续子数组，如果对这个子数组进行升序排序，
# 那么整个数组都会变为升序排序。请你找出符合题意的最短子数组，并输出它的长度。
#
# 示例：
# 输入：nums = [2,6,4,8,10,9,15]    输出：5
# 输入：nums = [1,2,3,4]            输出：0

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_seen = float("-inf")
        min_seen = float("inf")
        left, right = -1, -1

        for i in range(n):
            if nums[i] < max_seen:
                right = i
            else:
                max_seen = nums[i]

        for i in range(n - 1, -1, -1):
            if nums[i] > min_seen:
                left = i
            else:
                min_seen = nums[i]

        return 0 if right == -1 else right - left + 1


if __name__ == "__main__":
    s = Solution()
    print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))  # 5
    print(s.findUnsortedSubarray([1, 2, 3, 4]))             # 0
