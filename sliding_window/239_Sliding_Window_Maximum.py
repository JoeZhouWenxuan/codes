# 239. 滑动窗口最大值
# https://leetcode.cn/problems/sliding-window-maximum/
# 难度：困难
#
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组最左侧移动到最右侧。
# 返回每次窗口滑动时窗口中的最大值。
#
# 示例：
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3  输出：[3,3,5,5,6,7]
# 输入：nums = [1], k = 1                   输出：[1]
#
# 思路：固定窗口 + 单调队列。
# 队列里存下标，并保持对应值从队头到队尾单调递减。
# 队头下标永远对应当前窗口最大值。

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []

        for i, num in enumerate(nums):
            # 新元素入队前，弹出队尾所有小于等于它的元素。
            # 因为这些元素更小且更靠左，以后不可能再成为最大值。
            while queue and nums[queue[-1]] <= num:
                queue.pop()

            queue.append(i)

            # 如果队头已经滑出窗口 [i - k + 1, i]，就移除队头。
            if queue[0] <= i - k:
                queue.popleft()

            # 从第 k 个元素开始，每一步都能形成一个完整窗口。
            if i >= k - 1:
                ans.append(nums[queue[0]])

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
    print(s.maxSlidingWindow([1], 1))                         # [1]

