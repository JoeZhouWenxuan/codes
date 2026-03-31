# 48. 旋转图像
# https://leetcode.cn/problems/rotate-image/
# 难度：中等
#
# 给定一个 n x n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。
#
# 示例：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[7,4,1],[8,5,2],[9,6,3]]

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()


if __name__ == "__main__":
    s = Solution()
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(matrix1)
    print(matrix1)  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    s.rotate(matrix2)
    print(matrix2)  # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
