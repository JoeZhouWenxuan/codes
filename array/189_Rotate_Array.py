# 189. 轮转数组
# https://leetcode.cn/problems/rotate-array/
# 难度：中等
#
# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
#
# 示例：
# 输入：nums = [1,2,3,4,5,6,7], k = 3    输出：[5,6,7,1,2,3,4]

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(nums1, 3)
    print(nums1)  # [5, 6, 7, 1, 2, 3, 4]

    nums2 = [-1, -100, 3, 99]
    s.rotate(nums2, 2)
    print(nums2)  # [3, 99, -1, -100]
