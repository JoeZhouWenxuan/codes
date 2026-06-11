# 1854. 人口最多的年份
# https://leetcode.cn/problems/maximum-population-year/
# 难度：简单
#
# 题目：logs[i] = [birth, death]，人在 birth 年出生，death 年不再计入人口。
#
# 思路：
# 年份范围很小，直接用差分数组。birth 年 +1，death 年 -1。
# 扫描年份时维护人口，首次达到最大值的年份就是答案。

from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        base = 1950
        diff = [0] * 101
        for birth, death in logs:
            diff[birth - base] += 1
            diff[death - base] -= 1

        cur = best = 0
        ans = base
        for i in range(101):
            cur += diff[i]
            if cur > best:
                best = cur
                ans = base + i
        return ans


if __name__ == "__main__":
    print(Solution().maximumPopulation([[1993, 1999], [2000, 2010]]))  # 1993
