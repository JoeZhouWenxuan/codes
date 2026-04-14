# 240. 搜索二维矩阵 II
# https://leetcode.cn/problems/search-a-2d-matrix-ii/
# 难度：中等
#
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。
# 该矩阵具有以下特性：
# - 每行的元素从左到右升序排列
# - 每列的元素从上到下升序排列
#
# 示例：
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5   输出：True
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20  输出：False

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 思路：
        # 1. 从右上角开始搜索。
        # 2. 若当前值大于 target，说明这一列下面的数更大，不可能命中，向左移动。
        # 3. 若当前值小于 target，说明这一行左边的数更小，不可能命中，向下移动。
        # 4. 每一步都能排除一整行或一整列，时间复杂度 O(m + n)。
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1

        while row < rows and col >= 0:
            value = matrix[row][col]
            if value == target:
                return True
            if value > target:
                col -= 1
            else:
                row += 1

        return False


if __name__ == "__main__":
    s = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    print(s.searchMatrix(matrix, 5))   # True
    print(s.searchMatrix(matrix, 20))  # False
    print(s.searchMatrix([], 1))       # False
