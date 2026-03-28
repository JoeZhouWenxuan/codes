# 1. 两数之和
# https://leetcode.cn/problems/two-sum/
# 难度：简单
#
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
#
# 示例：
# 输入：nums = [2,7,11,15], target = 9    输出：[0,1]
# 输入：nums = [3,2,4], target = 6        输出：[1,2]

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i

        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(s.twoSum([3, 2, 4], 6))       # [1, 2]
