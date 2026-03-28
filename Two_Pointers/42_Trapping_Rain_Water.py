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
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        ans = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                ans += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                ans += right_max - height[right]
                right -= 1

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(s.trap([4, 2, 0, 3, 2, 5]))                    # 9
