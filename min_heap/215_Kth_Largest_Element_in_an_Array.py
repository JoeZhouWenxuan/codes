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
        # 解法一：小根堆
        # 维护一个大小为 k 的小根堆，堆顶始终是“当前前 k 大元素里最小的那个”。
        heap: List[int] = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

    def findKthLargestQuickSelect(self, nums: List[int], k: int) -> int:
        # 解法二：快选
        # 按“从大到小”分区，partition 后：
        # - 左边都比 pivot 大
        # - 右边都比 pivot 小或等于
        # 如果 pivot 正好落在下标 k - 1，上面就是第 k 大元素。
        def partition(l, r):
            index = random.randint(l, r)

            pivot_value = nums[index]
            nums[index], nums[r] = nums[r], nums[index]
            i = l
            for j in range(l, r):
                if nums[j] > pivot_value:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[r], nums[i] = nums[i], nums[r]
            return i

        left, right = 0, len(nums) - 1
        target = k - 1
        while True:
            index = partition(left, right)
            if index == target:
                return nums[index]
            elif index < target:
                left = index + 1
            else:
                right = index - 1


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))              # 5
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))     # 4
    print(s.findKthLargestQuickSelect([3, 2, 1, 5, 6, 4], 2))           # 5
    print(s.findKthLargestQuickSelect([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
