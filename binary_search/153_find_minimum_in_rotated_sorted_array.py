# 153. 寻找旋转排序数组中的最小值
# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/
# 难度：中等
#
# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次旋转后，得到输入数组。
# 给你一个元素值互不相同的数组 nums，找出并返回数组中的最小元素。
# 要求时间复杂度为 O(log n)。
#
# 示例：
# 输入：nums = [3,4,5,1,2]    输出：1
# 输入：nums = [4,5,6,7,0,1,2] 输出：0
# 输入：nums = [11,13,15,17]   输出：11

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # mid 在右半段（已旋转部分），最小值在左侧
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # mid 在左半段（有序部分），最小值在 mid 或左侧
                right = mid

        return nums[left]


if __name__ == "__main__":
    s = Solution()
    print(s.findMin([3, 4, 5, 1, 2]))      # 1
    print(s.findMin([4, 5, 6, 7, 0, 1, 2]))  # 0
    print(s.findMin([11, 13, 15, 17]))     # 11
