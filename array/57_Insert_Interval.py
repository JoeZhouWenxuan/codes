# 57. 插入区间
# https://leetcode.cn/problems/insert-interval/
# 难度：中等
#
# 给你一个无重叠的区间列表 intervals，按照区间起始端点排序。
# 在列表中插入一个新的区间 newInterval，你需要确保列表中的区间仍然有序且不重叠。
#
# 示例：
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]    输出：[[1,5],[6,9]]

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        ans.append(newInterval)

        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.insert([[1, 3], [6, 9]], [2, 5]))                  # [[1, 5], [6, 9]]
    print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # [[1, 2], [3, 10], [12, 16]]
