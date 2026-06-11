# 1109. 航班预订统计
# https://leetcode.cn/problems/corporate-flight-bookings/
# 难度：中等
#
# 题目：每条 booking = [first, last, seats]，表示 first 到 last 航班都增加 seats 个座位。
#
# 思路：
# 典型差分数组。注意航班编号从 1 开始，转成 0 下标处理。
# 对差分数组求前缀和后，就是每个航班的最终座位数。

from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)
        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats

        ans = []
        cur = 0
        for i in range(n):
            cur += diff[i]
            ans.append(cur)
        return ans


if __name__ == "__main__":
    print(Solution().corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5))
