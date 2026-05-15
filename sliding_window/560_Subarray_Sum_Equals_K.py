# 560. 和为 K 的子数组
# https://leetcode.cn/problems/subarray-sum-equals-k/
# 难度：中等
#
# 给你一个整数数组 nums 和一个整数 k，统计并返回该数组中和为 k 的连续子数组个数。
#
# 示例：
# 输入：nums = [1,1,1], k = 2    输出：2
# 输入：nums = [1,2,3], k = 3    输出：2
#
# 注意：这题属于“连续子数组”高频题，但不是普通滑动窗口。
# 因为 nums 可能包含负数，窗口和不具备单调性，所以用前缀和 + 哈希表。

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix_count[x] 表示前面出现过多少次前缀和 x。
        prefix_count = defaultdict(int)
        # 空前缀和为 0，出现 1 次。用于处理从下标 0 开始的子数组。
        prefix_count[0] = 1

        prefix = 0
        ans = 0

        for num in nums:
            prefix += num
            # 如果之前存在前缀和 prefix - k，
            # 那么中间这段子数组和就是 k。
            ans += prefix_count[prefix - k]
            prefix_count[prefix] += 1

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1, 1, 1], 2))  # 2
    print(s.subarraySum([1, 2, 3], 3))  # 2

