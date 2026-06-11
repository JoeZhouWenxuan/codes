# 303. 区域和检索 - 数组不可变
# https://leetcode.cn/problems/range-sum-query-immutable/
# 难度：简单
#
# 题目：多次查询 nums[left] 到 nums[right] 的区间和。
#
# 思路：
# 预处理前缀和 pre，其中 pre[i] 表示前 i 个元素之和。
# 区间 [left, right] 的和为 pre[right + 1] - pre[left]。

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.pre = [0]
        for num in nums:
            self.pre.append(self.pre[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right + 1] - self.pre[left]


if __name__ == "__main__":
    nums = NumArray([-2, 0, 3, -5, 2, -1])
    print(nums.sumRange(0, 2))  # 1
