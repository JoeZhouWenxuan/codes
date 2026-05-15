# 33. 搜索旋转排序数组
# https://leetcode.cn/problems/search-in-rotated-sorted-array/
# 难度：中等
#
# 整数数组 nums 按升序排列，数组中的值互不相同。
# 在传递给函数之前，nums 在预先未知的某个下标 k 上进行了旋转。
# 给你旋转后的数组 nums 和一个整数 target，如果 nums 中存在这个目标值 target，则返回它的下标，否则返回 -1。
#
# 示例：
# 输入：nums = [4,5,6,7,0,1,2], target = 0  输出：4
# 输入：nums = [4,5,6,7,0,1,2], target = 3  输出：-1

from typing import List


class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     left, right = 0, len(nums) - 1

    #     while left <= right:
    #         mid = (left + right) // 2

    #         if nums[mid] == target:
    #             return mid

    #         # 左半段有序
    #         if nums[left] <= nums[mid]:
    #             if nums[left] <= target < nums[mid]:
    #                 right = mid - 1
    #             else:
    #                 left = mid + 1
    #         # 右半段有序
    #         else:
    #             if nums[mid] < target <= nums[right]:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1

    #     return -1
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # 每次二分后，左右两边至少有一边是有序的。
            # 先判断左半段 [left, mid] 是否有序。
            if nums[left] <= nums[mid]:
                # target 落在左半段的有序范围内，继续去左边找。
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    # 否则 target 只能在右半段。
                    left = mid + 1
            else:
                # 否则右半段 [mid, right] 一定有序。
                # target 落在右半段的有序范围内，继续去右边找。
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    # 否则 target 只能在左半段。
                    right = mid - 1
        return -1 

if __name__ == "__main__":
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))   # 4
    print(s.search([4, 5, 6, 7, 0, 1, 2], 3))   # -1
    print(s.search([1], 0))                       # -1
