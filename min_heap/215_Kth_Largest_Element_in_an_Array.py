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
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = []

        # for num in nums:
        #     heapq.heappush(heap, num)
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # return heap[0]
        def quick_select(l, r, k):
            pivot = random.randint(l, r)
            pivot_v = nums[pivot]
            nums[r], nums[pivot]= nums[pivot], nums[r]

            j = l
            for i in range(l, r):
                if nums[i] > pivot_v:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1
            nums[i], nums[r] = nums[r], nums[i]

            rank = i - l + 1

            if rank == k:
                return nums[i]
            elif rank < k:
                return quick_select(i+1, r, k - rank)
            else:
                return quick_select(l, i-1, k)
            
        return quick_select(0, len(nums)-1, k)


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))              # 5
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))     # 4
