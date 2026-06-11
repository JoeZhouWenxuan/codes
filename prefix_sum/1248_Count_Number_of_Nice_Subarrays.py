# 1248. 统计优美子数组
# https://leetcode.cn/problems/count-number-of-nice-subarrays/
# 难度：中等
#
# 题目：统计恰好包含 k 个奇数的连续子数组个数。
#
# 思路：
# 把奇数看成 1，偶数看成 0，题目就变成统计和为 k 的子数组个数。
# 使用前缀和 + 哈希计数即可。

from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        odd_count = ans = 0

        for num in nums:
            odd_count += num % 2
            ans += count[odd_count - k]
            count[odd_count] += 1

        return ans


if __name__ == "__main__":
    print(Solution().numberOfSubarrays([1, 1, 2, 1, 1], 3))  # 2
