# 703. 数据流中的第 K 大元素
# https://leetcode.cn/problems/kth-largest-element-in-a-stream/
# 难度：简单
#
# 设计一个找到数据流中第 k 大元素的类。
#
# 示例：
# 输入：
# ["KthLargest","add","add","add","add","add"]
# [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
# 输出：
# [null,4,5,5,8,8]

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums[:]
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == "__main__":
    kth = KthLargest(3, [4, 5, 8, 2])
    print(kth.add(3))   # 4
    print(kth.add(5))   # 5
    print(kth.add(10))  # 5
    print(kth.add(9))   # 8
    print(kth.add(4))   # 8
