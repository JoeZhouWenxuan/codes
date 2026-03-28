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
        return [num for num, _ in Counter(nums).most_common(k)]
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        for x, freq in counts.items():
            if len(heap) < k:   # 应是小于，如果<=，再压进去就大于K
                heapq.heappush(heap, (freq, x))
            else:
                if heap[0][0] < freq:   # 新的元素大于才替换
                    heapq.heapreplace(heap, (freq, x))
        return [x for freq, x in heap]



if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    print(s.topKFrequent([1], 1))                 # [1]
