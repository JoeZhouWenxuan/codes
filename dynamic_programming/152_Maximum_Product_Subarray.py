# 152. 乘积最大子数组
# https://leetcode.cn/problems/maximum-product-subarray/
# 难度：中等
#
# 给你一个整数数组 nums，请你找出数组中乘积最大的非空连续子数组，并返回该子数组所对应的乘积。
#
# 示例：
# 输入：nums = [2,3,-2,4]    输出：6
# 输入：nums = [-2,0,-1]     输出：0

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 思路：
        # 1. 乘积和加法不同，负数会让最大值和最小值互换角色。
        # 2. 因此遍历到每个位置时，要同时维护“以当前位置结尾的最大乘积”和“最小乘积”。
        # 3. 当前数是负数时，上一轮的最小乘积乘上它，反而可能变成最大的。
        max_prod = min_prod = ans = nums[0]

        for num in nums[1:]:
            candidates = (num, max_prod * num, min_prod * num)
            max_prod = max(candidates)
            min_prod = min(candidates)
            ans = max(ans, max_prod)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2, 3, -2, 4]))   # 6
    print(s.maxProduct([-2, 0, -1]))     # 0
