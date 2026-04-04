# 85. 最大矩形
# https://leetcode.cn/problems/maximal-rectangle/
# 难度：困难
#
# 给定一个仅包含 0 和 1、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
# 示例：
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]    输出：6
# 输入：matrix = [["0"]]                                                                                      输出：0

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        ans = 0

        for row in matrix:
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max(ans, self.largestRectangleArea(heights))

        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        heights = [0] + heights + [0]
        for right, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                curr = stack.pop()
                left = stack[-1]
                width = right - left - 1

                ans = max(ans, heights[curr] * width)
            stack.append(right)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(
        s.maximalRectangle(
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ]
        )
    )  # 6
    print(s.maximalRectangle([["0"]]))  # 0
