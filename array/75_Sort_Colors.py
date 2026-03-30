# 75. 颜色分类
# https://leetcode.cn/problems/sort-colors/
# 难度：中等
#
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组 nums，原地对它们进行排序，
# 使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 我们使用整数 0、1 和 2 分别表示红色、白色和蓝色。
#
# 示例：
# 输入：nums = [2,0,2,1,1,0]    输出：[0,0,1,1,2,2]
# 输入：nums = [2,0,1]          输出：[0,1,2]

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        i = 0
        right = len(nums) - 1

        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            else:
                i += 1


if __name__ == "__main__":
    s = Solution()
    nums1 = [2, 0, 2, 1, 1, 0]
    s.sortColors(nums1)
    print(nums1)  # [0, 0, 1, 1, 2, 2]

    nums2 = [2, 0, 1]
    s.sortColors(nums2)
    print(nums2)  # [0, 1, 2]
