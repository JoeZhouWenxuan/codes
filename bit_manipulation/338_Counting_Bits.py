# 338. 比特位计数
# https://leetcode.cn/problems/counting-bits/
# 难度：简单
#
# 给你一个整数 n，对于 0 <= i <= n 中的每个 i，计算其二进制表示中 1 的个数，返回一个长度为 n + 1 的数组。
#
# 示例：
# 输入：n = 2    输出：[0,1,1]
# 输入：n = 5    输出：[0,1,1,2,1,2]

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp


if __name__ == "__main__":
    s = Solution()
    print(s.countBits(2))  # [0, 1, 1]
    print(s.countBits(5))  # [0, 1, 1, 2, 1, 2]
