# 167. 两数之和 II - 输入有序数组
# https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
# 难度：中等
#
# 给你一个下标从 1 开始的整数数组 numbers ，该数组已按非递减顺序排列，
# 请你从数组中找出满足相加之和等于目标数 target 的两个数。
#
# 示例：
# 输入：numbers = [2,7,11,15], target = 9    输出：[1,2]
# 输入：numbers = [2,3,4], target = 6        输出：[1,3]

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            if total < target:
                left += 1
            else:
                right -= 1

        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # [1, 2]
    print(s.twoSum([2, 3, 4], 6))       # [1, 3]
    print(s.twoSum([-1, 0], -1))        # [1, 2]
