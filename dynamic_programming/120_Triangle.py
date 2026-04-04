# 120. 三角形最小路径和
# https://leetcode.cn/problems/triangle/
# 难度：中等
#
# 给定一个三角形 triangle，找出自顶向下的最小路径和。
# 每一步只能移动到下一行中相邻的结点上。
#
# 示例：
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]    输出：11
# 输入：triangle = [[-10]]                          输出：-10

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 思路：
        # 1. dp[j] 表示“从当前处理行的第 j 个位置出发，到达底部的最小路径和”。
        # 2. 从最后一行开始往上推，当前格子只能走到下一行相邻的两个位置。
        # 3. 状态转移：dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        # 4. 最终 dp[0] 就是从顶点出发的最小路径和。
        dp = triangle[-1][:]

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]


if __name__ == "__main__":
    s = Solution()
    print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # 11
    print(s.minimumTotal([[-10]]))                                  # -10
