# 525. 连续数组
# https://leetcode.cn/problems/contiguous-array/
# 难度：中等
#
# 题目：给定二进制数组，找 0 和 1 数量相同的最长连续子数组长度。
#
# 思路：
# 把 0 看成 -1，把 1 看成 +1。若两处前缀和相同，中间这段和为 0，
# 即 0 和 1 数量相同。哈希表记录前缀和最早出现位置。

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first_pos = {0: -1}
        pre = ans = 0

        for i, num in enumerate(nums):
            pre += 1 if num == 1 else -1
            if pre in first_pos:
                ans = max(ans, i - first_pos[pre])
            else:
                first_pos[pre] = i

        return ans


if __name__ == "__main__":
    print(Solution().findMaxLength([0, 1, 0]))  # 2
