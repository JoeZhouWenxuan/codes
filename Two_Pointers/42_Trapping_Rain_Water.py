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


    def trap2(self, heights):
        '''
        这里通常写 while left < right 更合适。
        原因是当 left == right 时：
        只剩一个位置
        单独一根柱子不可能接住水
        再处理这一格没有意义
        所以双指针版 42 一般都写：

        while left < right:
        而不是：

        while left <= right:
        为什么不是 <=
        如果写 <=，在 left == right 那一轮：

        你还是会进入循环
        可能还会更新一次 left_max 或 right_max
        虽然很多实现最后结果未必错，但这一步是多余的
        也就是说：

        left < right：语义更准确，表示“两边至少得有两个边界”
        left <= right：通常不会更优，还容易让逻辑显得别扭
        一句话理解
        接雨水至少要有左右两边界，所以只剩一个指针位置时就该停。
        '''
        left, right = 0, len(heights) - 1
        left_max, right_max = 0
        ans = 0
        while left < right:
            if heights[left] < heights[right]:
                left_max = max(left_max, heights[left])
                ans += left_max - heights[left]
                left += 1
            else:
                right_max = max(right_max, heights[right])
                ans += right_max - heights[right]
                right -= 1
        
        return ans
            

        






if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(s.trap([4, 2, 0, 3, 2, 5]))                    # 9
