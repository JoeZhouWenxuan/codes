# 56. 合并区间
# https://leetcode.cn/problems/merge-intervals/
# 难度：中等
#
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]。
# 请你合并所有重叠的区间，并返回一个不重叠的区间数组。
#
# 示例：
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]    输出：[[1,6],[8,10],[15,18]]

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval[:])
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval[:])  # 拷贝
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
            

if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1, 6], [8, 10], [15, 18]]
    print(s.merge([[1, 4], [4, 5]]))                     # [[1, 5]]
