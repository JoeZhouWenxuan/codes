# 862. 和至少为 K 的最短子数组
# https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/
# 难度：困难
#
# 题目：返回和至少为 k 的非空连续子数组的最短长度，若不存在返回 -1。
#
# 思路：
# 构造前缀和 pre。需要找 j < i，使 pre[i] - pre[j] >= k 且 i - j 最小。
# 用单调队列维护前缀和递增的下标：当前 pre[i] 足够大时不断弹出队首更新答案；
# 若队尾前缀和大于等于当前值，它更晚且更大，不可能更优，弹出。

from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)

        queue = deque()
        ans = len(nums) + 1
        for i, value in enumerate(pre):
            while queue and value - pre[queue[0]] >= k:
                ans = min(ans, i - queue.popleft())
            while queue and pre[queue[-1]] >= value:
                queue.pop()
            queue.append(i)

        return ans if ans <= len(nums) else -1


if __name__ == "__main__":
    print(Solution().shortestSubarray([2, -1, 2], 3))  # 3
