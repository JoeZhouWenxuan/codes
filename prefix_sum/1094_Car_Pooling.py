# 1094. 拼车
# https://leetcode.cn/problems/car-pooling/
# 难度：中等
#
# 题目：trips[i] = [numPassengers, from, to]，乘客从 from 上车，到 to 下车，判断是否超载。
#
# 思路：
# 把每个站点的人数变化看成差分：from 增加乘客，to 减少乘客。
# 扫描站点并维护当前车上人数，若超过 capacity 则失败。

from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_pos = max(to for _, _, to in trips)
        diff = [0] * (max_pos + 1)

        for passengers, start, end in trips:
            diff[start] += passengers
            diff[end] -= passengers

        cur = 0
        for change in diff:
            cur += change
            if cur > capacity:
                return False
        return True


if __name__ == "__main__":
    print(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 4))  # False
