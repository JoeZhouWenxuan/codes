# 974. 和可被 K 整除的子数组
# https://leetcode.cn/problems/subarray-sums-divisible-by-k/
# 难度：中等
#
# 题目：统计和能被 k 整除的连续子数组个数。
#
# 思路：
# 若两个前缀和对 k 取模的结果相同，则它们之间的子数组和能被 k 整除。
# 统计每种余数出现次数，遍历时累加已有相同余数的数量。

from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        pre = ans = 0

        for num in nums:
            pre = (pre + num) % k
            ans += count[pre]
            count[pre] += 1

        return ans


if __name__ == "__main__":
    print(Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5))  # 7
