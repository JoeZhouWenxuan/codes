# 1590. 使数组和能被 P 整除
# https://leetcode.cn/problems/make-sum-divisible-by-p/
# 难度：中等
#
# 题目：删除最短的非空子数组，使剩余元素和能被 p 整除；不能删除整个数组。
#
# 思路：
# 总和余数 need = sum(nums) % p。需要删除一个子数组，其和 mod p 等于 need。
# 当前前缀余数为 cur，需要找之前的余数 target = (cur - need) % p。
# 为了最短长度，哈希表记录每个余数最近出现的位置。

from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        if need == 0:
            return 0

        last_pos = {0: -1}
        cur = 0
        ans = len(nums)

        for i, num in enumerate(nums):
            cur = (cur + num) % p
            target = (cur - need) % p
            if target in last_pos:
                ans = min(ans, i - last_pos[target])
            last_pos[cur] = i

        return ans if ans < len(nums) else -1


if __name__ == "__main__":
    print(Solution().minSubarray([3, 1, 4, 2], 6))  # 1
