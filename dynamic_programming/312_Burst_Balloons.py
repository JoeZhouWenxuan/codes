# 312. 戳气球
# https://leetcode.cn/problems/burst-balloons/
# 难度：困难
#
# 有 n 个气球，编号为 0 到 n - 1，每个气球上都标有一个数字。
# 戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。
# 求所能获得硬币的最大数量。
#
# 示例：
# 输入：nums = [3,1,5,8]    输出：167
# 输入：nums = [1,5]        输出：10

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        arr = [1] + nums + [1]
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                for last in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][last] + dp[last][right] + arr[left] * arr[last] * arr[right],
                    )

        return dp[0][n - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.maxCoins([3, 1, 5, 8]))  # 167
    print(s.maxCoins([1, 5]))        # 10
