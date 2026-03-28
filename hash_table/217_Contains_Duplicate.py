# 217. 存在重复元素
# https://leetcode.cn/problems/contains-duplicate/
# 难度：简单
#
# 给你一个整数数组 nums 。如果任一值在数组中出现至少两次，返回 true；如果数组中每个元素互不相同，返回 false。
#
# 示例：
# 输入：nums = [1,2,3,1]    输出：True
# 输入：nums = [1,2,3,4]    输出：False

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))  # True
    print(s.containsDuplicate([1, 2, 3, 4]))  # False
