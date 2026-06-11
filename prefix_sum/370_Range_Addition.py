# 370. 区间加法
# https://leetcode.cn/problems/range-addition/
# 难度：中等
#
# 题目：长度为 length 的数组初始全为 0，给出若干 [start, end, inc]，对区间整体加 inc。
#
# 思路：
# 使用差分数组 diff。区间 [l, r] 加 inc 等价于 diff[l] += inc，diff[r + 1] -= inc。
# 最后对 diff 做一次前缀和即可得到最终数组。

from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff = [0] * (length + 1)
        for start, end, inc in updates:
            diff[start] += inc
            if end + 1 < length:
                diff[end + 1] -= inc

        ans = [0] * length
        cur = 0
        for i in range(length):
            cur += diff[i]
            ans[i] = cur
        return ans


if __name__ == "__main__":
    print(Solution().getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]))
