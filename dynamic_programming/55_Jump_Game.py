# 55. 跳跃游戏
# https://leetcode.cn/problems/jump-game/
# 难度：中等
#
# 给定一个非负整数数组 nums，你最初位于数组的第一个下标。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度，判断你是否能够到达最后一个下标。
#
# 示例：
# 输入：nums = [2,3,1,1,4]    输出：True
# 输入：nums = [3,2,1,0,4]    输出：False

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # farthest = 0

        # for i, jump in enumerate(nums):
        #     if i > farthest:
        #         return False
        #     farthest = max(farthest, i + jump)

        # return True
        far = 0
        for i, num in enumerate(nums):
            if i > far:
                return False
            far = max(far, i + num)

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))  # True
    print(s.canJump([3, 2, 1, 0, 4]))  # False
