# 373. 查找和最小的 K 对数字
# https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/
# 难度：中等
#
# 给定两个以升序排列的整数数组 nums1 和 nums2，以及一个整数 k。
# 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2。
# 请找到和最小的 k 对数字。
#
# 示例：
# 输入：nums1 = [1,7,11], nums2 = [2,4,6], k = 3    输出：[[1,2],[1,4],[1,6]]

from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        heap = []
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        ans = []
        while heap and len(ans) < k:
            _, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))  # [[1, 2], [1, 4], [1, 6]]
