# 347. 前 K 个高频元素
# https://leetcode.cn/problems/top-k-frequent-elements/
# 难度：中等
#
# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。
#
# 示例：
# 输入：nums = [1,1,1,2,2,3], k = 2    输出：[1,2]
# 输入：nums = [1], k = 1              输出：[1]

from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for _, num in heap]


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(s.topKFrequent([1], 1))
