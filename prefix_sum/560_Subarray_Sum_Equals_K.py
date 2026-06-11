# 560. 和为 K 的子数组
# https://leetcode.cn/problems/subarray-sum-equals-k/
# 难度：中等
#
# 题目：统计和为 k 的连续子数组个数。
#
# 思路：
# 若当前前缀和为 pre，某个之前的前缀和为 pre - k，则这两个前缀之间的子数组和为 k。
# 用哈希表统计每个前缀和出现次数，边遍历边累加答案。

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        pre = ans = 0

        for num in nums:
            pre += num
            ans += count[pre - k]
            count[pre] += 1

        return ans


if __name__ == "__main__":
    print(Solution().subarraySum([1, 1, 1], 2))  # 2
