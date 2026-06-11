# 304. 二维区域和检索 - 矩阵不可变
# https://leetcode.cn/problems/range-sum-query-2d-immutable/
# 难度：中等
#
# 题目：多次查询矩阵中任意子矩形的元素和。
#
# 思路：
# 构造二维前缀和 pre，pre[i][j] 表示左上角到 matrix[i-1][j-1] 的区域和。
# 子矩形和 = 大矩形 - 上方 - 左方 + 左上角重复减掉的区域。

from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.pre[i + 1][j + 1] = (
                    self.pre[i][j + 1]
                    + self.pre[i + 1][j]
                    - self.pre[i][j]
                    + matrix[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pre = self.pre
        return (
            pre[row2 + 1][col2 + 1]
            - pre[row1][col2 + 1]
            - pre[row2 + 1][col1]
            + pre[row1][col1]
        )


if __name__ == "__main__":
    matrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5]])
    print(matrix.sumRegion(0, 0, 1, 1))  # 14
