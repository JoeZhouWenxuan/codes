# 34. 在排序数组中查找元素的第一个和最后一个位置
# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
# 难度：中等
#
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。
# 请你找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 要求时间复杂度为 O(log n)。
#
# 示例：
# 输入：nums = [5,7,7,8,8,10], target = 8  输出：[3,4]
# 输入：nums = [5,7,7,8,8,10], target = 6  输出：[-1,-1]

from typing import List


class Solution:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     def find_left(nums, target):
    #         left, right = 0, len(nums) - 1
    #         while left <= right:
    #             mid = (left + right) // 2
    #             if nums[mid] < target:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    #         return left

    #     left_idx = find_left(nums, target)
    #     if left_idx == len(nums) or nums[left_idx] != target:
    #         return [-1, -1]

    #     right_idx = find_left(nums, target + 1) - 1
    #     return [left_idx, right_idx]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        left_index = find_left(nums, target)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]
        right_index = find_left(nums, target+1) - 1

        return [left_index, right_index]



if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
    print(s.searchRange([5, 7, 7, 8, 8, 10], 6))  # [-1, -1]
    print(s.searchRange([], 0))                    # [-1, -1]
