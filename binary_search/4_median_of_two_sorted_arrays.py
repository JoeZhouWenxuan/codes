# 4. 寻找两个正序数组的中位数
# https://leetcode.cn/problems/median-of-two-sorted-arrays/
# 难度：困难
#
# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
# 请你找出并返回这两个正序数组的 中位数。
# 要求时间复杂度为 O(log(m+n))。
#
# 示例：
# 输入：nums1 = [1,3], nums2 = [2]         输出：2.00000
# 输入：nums1 = [1,2], nums2 = [3,4]       输出：2.50000

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保 nums1 是较短的数组，减少二分范围
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2  # nums1 左半部分取 i 个
            j = half - i             # nums2 左半部分取 j 个

            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]

            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # 找到正确划分
                left_max = max(nums1_left_max, nums2_left_max)
                if (m + n) % 2 == 1:
                    return float(left_max)
                right_min = min(nums1_right_min, nums2_right_min)
                return (left_max + right_min) / 2.0
            elif nums1_left_max > nums2_right_min:
                right = i - 1
            else:
                left = i + 1

        return 0.0
    def f(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2
        left, right = 0, m
        while left < right:
            i = (left+right) // 2
            j = half - i
            nums1_left_max = nums1[i-1] if i != 0 else float('-inf')
            nums1_right_min = nums1[i] if i != m else float('inf')
            nums2_left_max = nums2[j-1] if j != 0 else float('-inf')
            nums2_right_min = nums2[j] if j != n else float('inf')

            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                left_max = max(nums1_left_max, nums2_left_max)
                if (m+n) % 2 == 1:
                    return float(left_max)
                right_min = min(nums1_right_min, nums2_right_min)
                return (left_max + right_min) / 2.0
            elif nums1_left_max > nums2_right_min:
                right = i - 1
            else:
                left = i + 1
        return 0
    
    def f2(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m+n+1) // 2
        left = 0, right = m
        while left < right:
            i = (left+right)//2
            j = half - j

            nums1_left_max = nums1[i-1] if i != 0 else float('-inf')
            nums1_right_min = nums2[i] if i != m else float('inf')
            nums2_left_max = nums2[j-1] if j != 0 else float('-inf')
            nums2_right_min = nums2[j] if j != n else float('inf')
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                left_max = max(nums1_left_max, nums2_left_max)
                if (m+n) % 2 == 1:
                    return left_max
                right_min = min(nums1_right_min, nums2_right_min)
                return (left_max + right_min) // 2
            elif nums1_left_max > nums2_right_min:
                right -= 1
            else:
                left += 1
            

if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))        # 2.0
    print(s.findMedianSortedArrays([1, 2], [3, 4]))     # 2.5
    print(s.findMedianSortedArrays([0, 0], [0, 0]))     # 0.0
