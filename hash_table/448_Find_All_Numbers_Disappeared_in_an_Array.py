# 448. 找到所有数组中消失的数字
# https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/
# 难度：简单
#
# 给你一个含 n 个整数的数组 nums，其中 nums[i] 在区间 [1, n] 内。
# 请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组形式返回结果。
#
# 示例：
# 输入：nums = [4,3,2,7,8,2,3,1]    输出：[5,6]
# 输入：nums = [1,1]                输出：[2]

from typing import List


class Solution:
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     for num in nums:
    #         index = abs(num) - 1
    #         if nums[index] > 0:
    #             nums[index] = -nums[index]

    #     ans = []
    #     for i, num in enumerate(nums):
    #         if num > 0:
    #             ans.append(i + 1)

    #     return ans
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            index = abs(x) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        for i, x in enumerate(nums):
            if x > 0:
                ans.append(i+1)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))  # [5, 6]
    print(s.findDisappearedNumbers([1, 1]))                    # [2]
