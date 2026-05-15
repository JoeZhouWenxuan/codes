# 11. 盛最多水的容器
# https://leetcode.cn/problems/container-with-most-water/
# 难度：中等
#
# 给定一个长度为 n 的整数数组 height。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i])。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 示例：
# 输入：height = [1,8,6,2,5,4,8,3,7]    输出：49
# 输入：height = [1,1]                  输出：1

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left, right = 0, len(height) - 1
        # ans = 0

        # while left < right:
        #     width = right - left
        #     ans = max(ans, min(height[left], height[right]) * width)

        #     if height[left] < height[right]:
        #         left += 1
        #     else:
        #         right -= 1

        # return ans
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            width = right - left
            ans = max(ans, min(height[left], height[right]) * width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(s.maxArea([1, 1]))                       # 1
