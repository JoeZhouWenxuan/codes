# 1480. 一维数组的动态和
# https://leetcode.cn/problems/running-sum-of-1d-array/
# 难度：简单
#
# 题目：给定数组 nums，返回 runningSum，其中 runningSum[i] = nums[0] + ... + nums[i]。
#
# 思路：
# 从左到右累加当前元素，累加值就是当前位置的前缀和。
# 可以新建数组，也可以原地修改；这里用新数组，逻辑更清晰。

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        total = 0
        for num in nums:
            total += num
            ans.append(total)
        return ans


if __name__ == "__main__":
    print(Solution().runningSum([1, 2, 3, 4]))  # [1, 3, 6, 10]
