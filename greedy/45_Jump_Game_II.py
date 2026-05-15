# 45. 跳跃游戏 II
# https://leetcode.cn/problems/jump-game-ii/
# 难度：中等
#
# 给定一个非负整数数组 nums，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 返回到达最后一个位置的最小跳跃次数。
#
# 示例：
# 输入：nums = [2,3,1,1,4]  输出：2
# 输入：nums = [2,3,0,1,4]  输出：2
#
# 思路：贪心，按“层”扫描。
# 每一跳能覆盖一段区间，在这个区间内选择下一跳能到达最远的位置。

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # steps 表示已经跳了多少次。
        steps = 0
        # end 表示当前这一步能够覆盖到的最远边界。
        end = 0
        # farthest 表示在当前覆盖范围内，下一步最远能到达哪里。
        farthest = 0

        # 不需要遍历最后一个位置，因为到达最后一个位置后不用再跳。
        for i in range(len(nums) - 1):
            # 遍历当前这一步覆盖范围内的所有位置，记录下一步最远能到哪里。
            farthest = max(farthest, i + nums[i])

            # 走到当前覆盖边界，说明必须再跳一步。
            # 跳完后，下一步的覆盖边界更新为 farthest。
            if i == end:
                steps += 1
                end = farthest

        return steps


if __name__ == "__main__":
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))  # 2
    print(s.jump([2, 3, 0, 1, 4]))  # 2
