# 215. 数组中的第 K 个最大元素
# https://leetcode.cn/problems/kth-largest-element-in-an-array/
# 难度：中等
#
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
#
# 示例：
# 输入：nums = [3,2,1,5,6,4], k = 2    输出：5
# 输入：nums = [3,2,3,1,2,4,5,5,6], k = 4    输出：4

from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))              # 5
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))     # 4
