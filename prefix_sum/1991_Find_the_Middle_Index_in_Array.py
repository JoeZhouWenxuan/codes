# 1991. 找到数组的中间位置
# https://leetcode.cn/problems/find-the-middle-index-in-array/
# 难度：简单
#
# 题目：返回最左边的中间位置，使左侧和等于右侧和。
#
# 思路：
# 与 724 完全同型。遍历时维护左侧和，右侧和可由总和推出来。

from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i, num in enumerate(nums):
            if left == total - left - num:
                return i
            left += num
        return -1


if __name__ == "__main__":
    print(Solution().findMiddleIndex([2, 3, -1, 8, 4]))  # 3
