# 1314. 矩阵区域和
# https://leetcode.cn/problems/matrix-block-sum/
# 难度：中等
#
# 题目：对每个位置 (i, j)，求以它为中心、距离不超过 k 的矩形区域和。
#
# 思路：
# 先构造二维前缀和。每个位置的有效区域边界用 max/min 截断到矩阵范围内，
# 再用二维前缀和 O(1) 查询区域和。

from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pre[i + 1][j + 1] = pre[i][j + 1] + pre[i + 1][j] - pre[i][j] + mat[i][j]

        def region(r1: int, c1: int, r2: int, c2: int) -> int:
            return pre[r2 + 1][c2 + 1] - pre[r1][c2 + 1] - pre[r2 + 1][c1] + pre[r1][c1]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, c1 = max(0, i - k), max(0, j - k)
                r2, c2 = min(m - 1, i + k), min(n - 1, j + k)
                ans[i][j] = region(r1, c1, r2, c2)
        return ans


if __name__ == "__main__":
    print(Solution().matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
