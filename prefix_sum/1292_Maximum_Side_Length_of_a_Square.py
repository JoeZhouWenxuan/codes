# 1292. 元素和小于等于阈值的正方形的最大边长
# https://leetcode.cn/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
# 难度：中等
#
# 题目：在矩阵中找元素和不超过 threshold 的最大正方形边长。
#
# 思路：
# 用二维前缀和 O(1) 查询任意正方形和。
# 枚举边长从小到大，若存在合法正方形就更新答案。因为边长最多 min(m, n)，足够清晰。

from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pre[i + 1][j + 1] = pre[i][j + 1] + pre[i + 1][j] - pre[i][j] + mat[i][j]

        def square_sum(r: int, c: int, size: int) -> int:
            return pre[r + size][c + size] - pre[r][c + size] - pre[r + size][c] + pre[r][c]

        ans = 0
        for size in range(1, min(m, n) + 1):
            ok = False
            for r in range(m - size + 1):
                for c in range(n - size + 1):
                    if square_sum(r, c, size) <= threshold:
                        ok = True
                        break
                if ok:
                    break
            if ok:
                ans = size
        return ans


if __name__ == "__main__":
    print(Solution().maxSideLength([[1, 1, 3], [1, 1, 3], [3, 3, 3]], 4))  # 2
