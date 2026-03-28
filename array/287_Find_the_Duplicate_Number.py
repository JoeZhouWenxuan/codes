# 287. 寻找重复数
# https://leetcode.cn/problems/find-the-duplicate-number/
# 难度：中等
#
# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 [1, n] 范围内，可知至少存在一个重复的整数。
# 假设 nums 只有一个重复的整数，返回这个重复的数。
#
# 示例：
# 输入：nums = [1,3,4,2,2]    输出：2
# 输入：nums = [3,1,3,4,2]    输出：3

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate([1, 3, 4, 2, 2]))  # 2
    print(s.findDuplicate([3, 1, 3, 4, 2]))  # 3
