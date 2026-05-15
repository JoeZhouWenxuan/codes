# 55. 跳跃游戏
# https://leetcode.cn/problems/jump-game/
# 难度：中等
#
# 给定一个非负整数数组 nums，你最初位于数组的第一个下标。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度，判断是否能够到达最后一个下标。
#
# 示例：
# 输入：nums = [2,3,1,1,4]  输出：True
# 输入：nums = [3,2,1,0,4]  输出：False

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # farthest 表示当前能够到达的最远下标。
        farthest = 0

        for i, jump in enumerate(nums):
            # 如果当前位置 i 已经超过最远可达位置，说明无法走到这里。
            if i > farthest:
                return False

            # 从当前位置起跳，尝试更新最远可达位置。
            farthest = max(farthest, i + jump)

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))  # True
    print(s.canJump([3, 2, 1, 0, 4]))  # False

