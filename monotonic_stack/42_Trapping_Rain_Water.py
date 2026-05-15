# 42. 接雨水
# https://leetcode.cn/problems/trapping-rain-water/
# 难度：困难
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
# 示例：
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]    输出：6
# 输入：height = [4,2,0,3,2,5]                输出：9

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 单调递减栈，栈里存柱子的下标。
        # 当遇到比栈顶更高的柱子时，说明可能形成了一个“凹槽”，可以计算接水量。
        stack = []
        ans = 0

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                # bottom 是凹槽底部。
                bottom = stack.pop()
                # 如果弹出后左边没有柱子，就无法形成左右边界，不能接水。
                if not stack:
                    break
                # left 是凹槽左边界，当前 i 是凹槽右边界。
                left = stack[-1]
                # 左右边界之间的距离减 1，就是这层水的宽度。
                width = i - left - 1
                # 水位由左右边界中较矮的一边决定，再减去底部高度。
                bounded_height = min(height[left], h) - height[bottom]
                ans += width * bounded_height
            # 当前柱子入栈，等待后续更高的右边界来结算。
            stack.append(i)

        return ans
    


    def trap_two_pointers(self, height: List[int]) -> int:
        # left, right = 0, len(height) - 1
        # left_max, right_max = 0, 0
        # ans = 0

        # while left < right:
        #     if height[left] < height[right]:
        #         left_max = max(left_max, height[left])
        #         ans += left_max - height[left]
        #         left += 1
        #     else:
        #         right_max = max(right_max, height[right])
        #         ans += right_max - height[right]
        #         right -= 1

        # return ans
        left, right = 0, len(height) - 1
        # left_max 表示 left 左侧及当前位置见过的最高柱子。
        # right_max 表示 right 右侧及当前位置见过的最高柱子。
        left_max, right_max = 0, 0
        ans = 0
        while left < right:
            # 哪一侧更矮，就先结算哪一侧。
            # 因为较矮侧的最大水位已经受这一侧的 max 限制，另一侧至少有当前更高的边界兜住。
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                # 当前 left 能接的水 = 左侧最高柱子 - 当前柱子高度。
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                # 当前 right 能接的水 = 右侧最高柱子 - 当前柱子高度。
                ans += right_max - height[right]
                right -= 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))               # 6
    print(s.trap([4, 2, 0, 3, 2, 5]))                                   # 9
    print(s.trap_two_pointers([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(s.trap_two_pointers([4, 2, 0, 3, 2, 5]))                     # 9
