# 560. 和为 K 的子数组
# https://leetcode.cn/problems/subarray-sum-equals-k/
# 难度：中等
#
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的子数组的个数。
#
# 示例：
# 输入：nums = [1,1,1], k = 2    输出：2
# 输入：nums = [1,2,3], k = 3    输出：2

from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix_count = defaultdict(int)
        # prefix_count[0] = 1
        # prefix = 0
        # ans = 0

        # for num in nums:
        #     prefix += num
        #     ans += prefix_count[prefix - k]
        #     prefix_count[prefix] += 1

        # return ans
        ans = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num
            ans += prefix_count[prefix - k]
            prefix_count[prefix] += 1
        return ans
    
    def subarraySum2(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        prefix = 0
        ans = 0

        for x in nums:
            prefix += x
            ans += prefix_count.get(prefix - k, 0)
            prefix_count[prefix] = prefix_count.get(prefix, 0) + 1

        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1, 1, 1], 2))  # 2
    print(s.subarraySum([1, 2, 3], 3))  # 2
