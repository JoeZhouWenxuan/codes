# 215. 数组中的第K个最大元素
# https://leetcode.cn/problems/kth-largest-element-in-an-array/
# 难度：中等
#
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
# 要求不能对数组进行排序。
#
# 示例：
# nums = [3,2,1,5,6,4], k=2 → 5
# nums = [3,2,3,1,2,4,5,5,6], k=4 → 4


import heapq
import random


# ── 方法一：小顶堆 O(n log k) 时间，O(k) 空间 ──────────────────────────────
#
# 维护一个大小为 k 的小顶堆：
#   - 堆顶始终是堆中最小值
#   - 遍历数组，若当前元素 > 堆顶，弹出堆顶并压入当前元素
#   - 遍历结束后堆中保留了最大的 k 个数，堆顶即第 k 大
#
# 为什么用小顶堆而不是大顶堆？
#   大顶堆需要把所有元素压入再弹出 k 次，O(n + k log n)
#   小顶堆只维护 k 个元素，每次操作 O(log k)，更适合 k << n 的场景
class SolutionHeap:
    def findKthLargest(self, nums: list, k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)   # 弹出最小值，保持堆大小为 k
        return heap[0]                # 堆顶 = 第 k 大


# ── 方法二：快速选择 QuickSelect O(n) 均摊，O(1) 额外空间 ──────────────────
#
# 基于快速排序的 partition 思想：
#   每次随机选一个基准 pivot，将数组分为「大于 pivot」和「小于 pivot」两部分。
#   - 若左侧（大于 pivot）元素个数 == k-1，pivot 就是答案
#   - 若左侧元素个数 >= k，答案在左侧，递归左侧
#   - 否则答案在右侧，递归右侧（k 减去左侧个数和 pivot 自身）
#
# 随机化 pivot 使期望时间复杂度为 O(n)，避免最坏 O(n²)
class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        # def quick_select(lo, hi, k):
        #     # 随机选 pivot，交换到末尾
        #     pivot_idx = random.randint(lo, hi)
        #     nums[pivot_idx], nums[hi] = nums[hi], nums[pivot_idx]
        #     pivot = nums[hi]

        #     # partition：将大于 pivot 的放左边
        #     store = lo
        #     for i in range(lo, hi):
        #         if nums[i] > pivot:
        #             nums[store], nums[i] = nums[i], nums[store]
        #             store += 1
        #     nums[store], nums[hi] = nums[hi], nums[store]

        #     # store 位置就是 pivot 的最终位置
        #     rank = store - lo + 1   # pivot 是当前范围内第 rank 大
        #     if rank == k:
        #         return nums[store]
        #     elif rank > k:
        #         return quick_select(lo, store - 1, k)
        #     else:
        #         return quick_select(store + 1, hi, k - rank)

        # return quick_select(0, len(nums) - 1, k)
    
        def quick_select(l, r, k):
            pivot_index = random.randint(l, r)
            nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
            pivot_value = nums[r]

            index = l
            for i in range(l, r):
                if nums[i] > pivot_value:
                    nums[index], nums[i] = nums[i], nums[index]
                    index += 1
            nums[index], nums[r] = nums[r], nums[index]
                
            
            rank = index - l + 1
            if rank == k:
                return nums[index]
            elif rank > k:
                return quick_select(l, index - 1, k)
            else:
                return quick_select(index + 1, r, k - rank)
        return quick_select(0, len(nums) - 1, k)


if __name__ == "__main__":
    heap_sol = SolutionHeap()
    qs_sol   = Solution()

    cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([2, 1], 1, 2),
    ]
    for nums, k, expected in cases:
        r1 = heap_sol.findKthLargest(nums[:], k)
        r2 = qs_sol.findKthLargest(nums[:], k)
        status = "✓" if r1 == r2 == expected else "✗"
        print(f"{status} nums={nums}, k={k}  heap={r1}  quickselect={r2}  expected={expected}")
