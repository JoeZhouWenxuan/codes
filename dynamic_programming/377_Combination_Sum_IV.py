# 377. 组合总和 IV
# https://leetcode.cn/problems/combination-sum-iv/
# 难度：中等
#
# 给你一个由不同整数组成的数组 nums 和一个目标整数 target。
# 返回可以使数字和为 target 的组合个数，顺序不同的序列被视作不同组合。
#
# 示例：
# 输入：nums = [1,2,3], target = 4    输出：7
#
# 和爬楼梯关系：
# 如果 nums = [1, 2]，target = n，这题就退化成 70. 爬楼梯。
# 区别是这里的可选步长来自 nums，而且顺序不同算不同方案。

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp[i] 表示凑出总和 i 的排列方案数。
        dp = [0] * (target + 1)
        # 凑出 0 有 1 种方式：什么都不选。它是后续转移的起点。
        dp[0] = 1

        # 外层枚举总和，内层枚举最后一步选哪个 num。
        # 这样会把不同顺序计为不同方案。
        for total in range(1, target + 1):
            for num in nums:
                if total >= num:
                    dp[total] += dp[total - num]

        return dp[target]


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum4([1, 2, 3], 4))  # 7
    print(s.combinationSum4([1, 2], 3))     # 3

