# 1524. 和为奇数的子数组数目
# https://leetcode.cn/problems/number-of-sub-arrays-with-odd-sum/
# 难度：中等
#
# 题目：统计和为奇数的连续子数组个数，答案对 1e9 + 7 取模。
#
# 思路：
# 子数组和为奇数，等价于两个前缀和奇偶性不同。
# 遍历时记录已有偶数前缀和、奇数前缀和数量，当前奇偶性与相反奇偶性配对。

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        count = [1, 0]
        parity = ans = 0

        for num in arr:
            parity = (parity + num) % 2
            ans = (ans + count[1 - parity]) % mod
            count[parity] += 1

        return ans


if __name__ == "__main__":
    print(Solution().numOfSubarrays([1, 3, 5]))  # 4
