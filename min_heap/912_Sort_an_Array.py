# 912. 排序数组
# https://leetcode.cn/problems/sort-an-array/
# 难度：中等
#
# 给你一个整数数组 nums，请你将该数组升序排列。
#
# 这题本身不限定必须使用堆，但如果想练：
# - buildHeap
# - heapify / siftDown
# - 原地堆排序
# 它是 LeetCode 里最适合拿来练“建堆”动作的代表题之一。

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 堆排序通常使用大根堆，这样每轮都能把当前最大值放到数组末尾。
        self.buildMaxHeap(nums)

        for end in range(len(nums) - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            self.siftDownMax(nums, 0, end)

        return nums

    def buildMinHeap(self, nums: List[int]) -> List[int]:
        # 这个辅助函数专门保留给“小根堆建堆”练习使用。
        for i in range(len(nums) // 2 - 1, -1, -1):
            self.siftDownMin(nums, i, len(nums))
        return nums

    def buildMaxHeap(self, nums: List[int]) -> None:
        for i in range(len(nums) // 2 - 1, -1, -1):
            self.siftDownMax(nums, i, len(nums))

    def siftDownMin(self, nums: List[int], i: int, size: int) -> None:
        while True:
            smallest = i
            left = i * 2 + 1
            right = i * 2 + 2

            if left < size and nums[left] < nums[smallest]:
                smallest = left
            if right < size and nums[right] < nums[smallest]:
                smallest = right

            if smallest == i:
                return

            nums[i], nums[smallest] = nums[smallest], nums[i]
            i = smallest

    def siftDownMax(self, nums: List[int], i: int, size: int) -> None:
        while True:
            largest = i
            left = i * 2 + 1
            right = i * 2 + 2

            if left < size and nums[left] > nums[largest]:
                largest = left
            if right < size and nums[right] > nums[largest]:
                largest = right

            if largest == i:
                return

            nums[i], nums[largest] = nums[largest], nums[i]
            i = largest


if __name__ == "__main__":
    s = Solution()

    nums1 = [5, 2, 3, 1]
    print(s.sortArray(nums1))  # [1, 2, 3, 5]

    nums2 = [5, 1, 4, 2, 8, 0]
    print(s.buildMinHeap(nums2))  # 一个合法的小根堆形态，例如 [0, 1, 4, 2, 8, 5]
