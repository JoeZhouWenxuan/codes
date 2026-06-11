# 1074. 元素和为目标值的子矩阵数量
# https://leetcode.cn/problems/number-of-submatrices-that-sum-to-target/
# 难度：困难
#
# 题目：统计矩阵中元素和等于 target 的非空子矩阵数量。
#
# 思路：
# 枚举上下边界，把两行之间的每一列压缩成一维数组 col_sums。
# 问题变成“统计一维数组中和为 target 的子数组个数”，直接套 560 模板。

from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0

        for top in range(m):
            col_sums = [0] * n
            for bottom in range(top, m):
                for col in range(n):
                    col_sums[col] += matrix[bottom][col]

                count = defaultdict(int)
                count[0] = 1
                pre = 0
                for value in col_sums:
                    pre += value
                    ans += count[pre - target]
                    count[pre] += 1

        return ans


if __name__ == "__main__":
    print(Solution().numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0))  # 4
