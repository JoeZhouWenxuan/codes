# 31. 下一个排列
# https://leetcode.cn/problems/next-permutation/
# 难度：中等
#
# 整数数组的下一个排列是指其整数的下一个字典序更大的排列。
# 如果不存在下一个更大的排列，则将数组重新排列成最小的排列（即升序排列）。
# 必须 原地 修改，只允许使用额外常数空间。
#
# 示例：
# [1,2,3] → [1,3,2]
# [3,2,1] → [1,2,3]
# [1,1,5] → [1,5,1]
#
# ┌──────────────────────────────────────────────────────────────┐
# │ 解法对比                                                      │
# │  1. 标准原地算法   O(n) 时间  O(1) 空间   唯一推荐解法        │
# │  2. 暴力枚举       O(n! · n)  O(n!)空间   仅用于理解正确性    │
# └──────────────────────────────────────────────────────────────┘

from typing import List
from itertools import permutations


# ── 解法一：标准原地算法 ───────────────────────────────────────
# 核心观察：下一个排列 = 尽量靠右地做一次"最小的升级"
# 步骤：
#   1. 从右向左找第一个"下降点" i，满足 nums[i] < nums[i+1]
#      （i 右侧是非递增的，已经是该后缀的最大排列）
#   2. 若找不到 i，整个数组降序，直接反转返回最小排列
#   3. 从右向左找第一个比 nums[i] 大的 j，交换 nums[i] 与 nums[j]
#   4. 反转 i+1 到末尾（使后缀变为最小的升序）
# 时间 O(n)，空间 O(1)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # 步骤 1：找下降点 i
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # 步骤 3：找右侧第一个比 nums[i] 大的 j
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 步骤 4：反转 i+1 到末尾
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # n = len(nums)
        # i = n - 2
        # while i >= 0 and nums[i] >= nums[i + 1]:
        #     i -= 1
        # if i >= 0:
        #     j = n - 1
        #     while nums[j] <= nums[i]:
        #         j -= 1
        #     nums[i], nums[j] = nums[j], nums[i]
        # left, right = i + 1, n - 1
        # while left < right:
        #     nums[left], nums[right] = nums[right], nums[left]
        #     left += 1
        #     right -= 1

# ── 解法二：暴力枚举 ──────────────────────────────────────────
# 生成所有排列排序后找当前排列的下一个。
# 时间 O(n! · n)，空间 O(n!)，仅用于验证解法一的正确性。
class Solution2:
    def nextPermutation(self, nums: List[int]) -> None:
        all_perms = sorted(set(permutations(nums)))
        cur = tuple(nums)
        idx = all_perms.index(cur)
        nxt = all_perms[(idx + 1) % len(all_perms)]
        nums[:] = list(nxt)


if __name__ == "__main__":
    cases = [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5, 3, 2, 1], [1, 2, 1, 1, 3, 5]),
        ([1],       [1]),
    ]

    for Cls in [Solution, Solution2]:
        print(Cls.__name__)
        for nums, expected in cases:
            inp = nums[:]
            Cls().nextPermutation(inp)
            status = "OK" if inp == expected else f"FAIL (got {inp})"
            print(f"  {nums} → {inp}  {status}")
