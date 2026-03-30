# 84. 柱状图中最大的矩形
# https://leetcode.cn/problems/largest-rectangle-in-histogram/
# 难度：困难
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1。
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
# 示例：
# 输入：heights = [2,1,5,6,2,3]    输出：10
# 输入：heights = [2,4]            输出：4

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack = []
        # ans = 0
        # extended = heights + [0]

        # for i, h in enumerate(extended):
        #     while stack and extended[stack[-1]] > h:
        #         height = extended[stack.pop()]
        #         left = stack[-1] if stack else -1
        #         width = i - left - 1
        #         ans = max(ans, height * width)
        #     stack.append(i)
        # return ans
        stack = []
        ans = 0
        heights = [0] + heights + [0]
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1]
                width = i - left - 1
                ans = max(ans, height * width)
            stack.append(i)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
    print(s.largestRectangleArea([2, 4]))              # 4
