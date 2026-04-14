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
        '''
        这题的代码核心是“区间 DP + 枚举最后一个被戳破的气球”
        '''
        '''
        定义：
        dp[left][right]
        表示：

        戳破开区间 (left, right) 内所有气球，能得到的最大硬币数。

        注意是开区间，不包括 left 和 right 自己。

        比如：

        dp[0][5] 表示戳破 arr[1] ~ arr[4]
        dp[1][4] 表示戳破 arr[2] ~ arr[3]


        3. 为什么要枚举“最后一个戳破的气球”
        这题正着想很难，因为：

        你先戳哪个，会影响后面左右邻居
        状态一直在变
        所以反过来想：

        假设区间 (left, right) 里，最后一个被戳的是 last。

        那这时候：

        last 左边的气球都已经戳完了
        last 右边的气球也已经戳完了
        所以它最终相邻的一定就是 left 和 right
        于是最后戳 last 的收益就固定了：

        arr[left] * arr[last] * arr[right]
        '''
        # arr = [1] + nums + [1]
        # n = len(arr)
        # dp = [[0] * n for _ in range(n)]

        # for length in range(2, n):
        #     for left in range(0, n - length):
        #         right = left + length
        #         for last in range(left + 1, right):
        #             dp[left][right] = max(
        #                 dp[left][right],
        #                 dp[left][last] + dp[last][right] + arr[left] * arr[last] * arr[right],
        #             )

        # return dp[0][n - 1]
        arr = [1] + nums + [1]
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for len in range(2, n):
            for left in range(0, n - len):
                right = left + len
                for last in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right], 
                        dp[left][last] + dp[last][right] + arr[left]* arr[last]* arr[right]
                    )
        return dp[0][n-1]


if __name__ == "__main__":
    s = Solution()
    print(s.maxCoins([3, 1, 5, 8]))  # 167
    print(s.maxCoins([1, 5]))        # 10
