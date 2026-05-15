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
        # 单调递增栈，栈里存的是柱子的下标，且对应高度从栈底到栈顶递增。
        # 当遇到更矮的柱子时，说明栈顶柱子的右边界已经确定，可以计算面积。
        stack = []
        ans = 0
        # 左右各加一个高度为 0 的哨兵：
        # 左哨兵避免栈空时单独处理边界，右哨兵保证最后所有柱子都会被弹出计算。
        heights = [0] + heights + [0]
        for i, h in enumerate(heights):
            # 当前高度 h 比栈顶柱子矮，栈顶柱子无法再向右延伸。
            while stack and heights[stack[-1]] > h:
                # 弹出的柱子作为矩形高度。
                height = heights[stack.pop()]
                # 弹出后新的栈顶，是左侧第一个比 height 小的柱子。
                left = stack[-1]
                # 当前 i 是右侧第一个比 height 小的柱子。
                # 因此矩形宽度是两个较矮柱子之间的距离减 1。
                width = i - left - 1
                ans = max(ans, height * width)
            # 当前柱子还没确定右边界，入栈等待后续更矮的柱子触发计算。
            stack.append(i)
        return ans
    
if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
    print(s.largestRectangleArea([2, 4]))              # 4
