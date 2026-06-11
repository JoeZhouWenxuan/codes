# 238. 除自身以外数组的乘积
# https://leetcode.cn/problems/product-of-array-except-self/
# 难度：中等
#
# 给你一个整数数组 nums，返回数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#
# 示例：
# 输入：nums = [1,2,3,4]    输出：[24,12,8,6]

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # ans = [1] * n

        # prefix = 1
        # for i in range(n):
        #     ans[i] = prefix
        #     prefix *= nums[i]

        # suffix = 1
        # for i in range(n - 1, -1, -1):
        #     ans[i] *= suffix
        #     suffix *= nums[i]

        # return ans
        n = len(nums)
        ans = [1] * n
        prefix = 1
        for i, num in enumerate(nums):
            ans[i] *= prefix
            prefix *= num
        suffix = 1
        for j in range(len(nums) - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[j]

        return ans



if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))     # [24, 12, 8, 6]
    print(s.productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
