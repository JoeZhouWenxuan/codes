# 523. 连续的子数组和
# https://leetcode.cn/problems/continuous-subarray-sum/
# 难度：中等
#
# 题目：判断是否存在长度至少为 2 的子数组，其和是 k 的倍数。
#
# 思路：
# 两个前缀和对 k 的余数相同，则它们之间的子数组和能被 k 整除。
# 哈希表记录每个余数最早出现的位置，并检查距离是否至少为 2。

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        first_pos = {0: -1}
        pre = 0

        for i, num in enumerate(nums):
            pre = (pre + num) % k
            if pre in first_pos:
                if i - first_pos[pre] >= 2:
                    return True
            else:
                first_pos[pre] = i

        return False


if __name__ == "__main__":
    print(Solution().checkSubarraySum([23, 2, 4, 6, 7], 6))  # True
