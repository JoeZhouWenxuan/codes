# 724. 寻找数组的中心下标
# https://leetcode.cn/problems/find-pivot-index/
# 难度：简单
#
# 题目：找到一个下标，使其左侧元素和等于右侧元素和。
#
# 思路：
# 设总和为 total，遍历时维护左侧和 left。
# 当前下标 i 满足 left == total - left - nums[i] 时就是答案。

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i, num in enumerate(nums):
            if left == total - left - num:
                return i
            left += num
        return -1


if __name__ == "__main__":
    print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))  # 3
