# 930. 和相同的二元子数组
# https://leetcode.cn/problems/binary-subarrays-with-sum/
# 难度：中等
#
# 题目：给定只含 0 和 1 的数组 nums，统计和为 goal 的非空子数组个数。
#
# 思路：
# 仍然是 560 的模板。当前前缀和为 pre，之前出现过 pre - goal 几次，就能形成几个答案。

from collections import defaultdict
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        pre = ans = 0

        for num in nums:
            pre += num
            ans += count[pre - goal]
            count[pre] += 1

        return ans


if __name__ == "__main__":
    print(Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2))  # 4
