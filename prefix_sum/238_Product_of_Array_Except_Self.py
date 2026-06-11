# 238. 除自身以外数组的乘积
# https://leetcode.cn/problems/product-of-array-except-self/
# 难度：中等
#
# 题目：返回数组 answer，answer[i] 等于 nums 中除 nums[i] 外其余元素的乘积。
#
# 思路：
# 这是前缀积 + 后缀积。先让 ans[i] 保存 i 左侧所有元素乘积；
# 再从右往左维护右侧乘积 right，并乘到 ans[i] 上。

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        left = 1
        for i, num in enumerate(nums):
            ans[i] = left
            left *= num

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]

        return ans


if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
