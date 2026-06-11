# 325. 和等于 k 的最长子数组长度
# https://leetcode.cn/problems/maximum-size-subarray-sum-equals-k/
# 难度：中等
#
# 题目：返回和为 k 的最长连续子数组长度。
#
# 思路：
# 当前前缀和为 pre，需要找最早出现的 pre - k。
# 哈希表只记录每个前缀和第一次出现的位置，这样长度最大。

from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        first_pos = {0: -1}
        pre = ans = 0

        for i, num in enumerate(nums):
            pre += num
            if pre - k in first_pos:
                ans = max(ans, i - first_pos[pre - k])
            if pre not in first_pos:
                first_pos[pre] = i

        return ans


if __name__ == "__main__":
    print(Solution().maxSubArrayLen([1, -1, 5, -2, 3], 3))  # 4
