# 283. 移动零
# https://leetcode.cn/problems/move-zeroes/
# 难度：简单
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意，必须在不复制数组的情况下原地对数组进行操作。
#
# 示例：
# 输入：nums = [0,1,0,3,12]    输出：[1,3,12,0,0]
# 输入：nums = [0]             输出：[0]

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # slow = 0

        # for fast in range(len(nums)):
        #     if nums[fast] != 0:
        #         nums[slow], nums[fast] = nums[fast], nums[slow]
        #         slow += 1
        slow = 0
        for fast, num in enumerate(nums):
            if num != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1   # slow 在判断分支内部
        

if __name__ == "__main__":
    s = Solution()
    nums1 = [0, 1, 0, 3, 12]
    s.moveZeroes(nums1)
    print(nums1)  # [1, 3, 12, 0, 0]

    nums2 = [0]
    s.moveZeroes(nums2)
    print(nums2)  # [0]
