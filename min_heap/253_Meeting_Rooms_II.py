# 253. 会议室 II
# https://leetcode.cn/problems/meeting-rooms-ii/
# 难度：中等
#
# 给定一个会议时间安排的数组 intervals，每个会议时间都会包括开始和结束的时间
# intervals[i] = [start_i, end_i]，请你计算至少需要多少间会议室，才能满足这些会议安排。
#
# 示例：
# 输入：intervals = [[0,30],[5,10],[15,20]]    输出：2
# 输入：intervals = [[7,10],[2,4]]             输出：1

import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 思路：
        # 1. 先按会议开始时间排序，按“时间线”依次处理每个会议。
        # 2. 小根堆里只存“当前正在占用中的会议结束时间”。
        # 3. 堆顶就是最早结束的会议，也就是最早能空出来的会议室。
        # 4. 如果当前会议开始时间 >= 堆顶结束时间，说明最早那间会议室已经空出来了，可以复用。
        # 5. 这题本质上是在求同一时刻最多有多少个区间重叠。
        # if not intervals:
        #     return 0

        # intervals.sort()
        # min_heap: List[int] = []

        # for start, end in intervals:
        #     if min_heap and start >= min_heap[0]:
        #         heapq.heappop(min_heap)
        #     heapq.heappush(min_heap, end)

        # return len(min_heap)
        if not intervals:
            return 0
        heap = []
        for start, end in intervals:
            if heap and heap[0] <= start: # 如果当前会议开始时间 >= 堆顶结束时间，说明最早那间会议室已经空出来了，可以复用。
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return len(heap)

if __name__ == "__main__":
    s = Solution()
    print(s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))  # 2
    print(s.minMeetingRooms([[7, 10], [2, 4]]))             # 1
    print(s.minMeetingRooms([]))                            # 0
