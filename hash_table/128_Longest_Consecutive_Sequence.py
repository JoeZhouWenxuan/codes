# 128. 最长连续序列
# https://leetcode.cn/problems/longest-consecutive-sequence/
# 难度：中等
#
# 给定一个未排序的整数数组 nums，找出数字连续的最长序列长度。
#
# 示例：
# 输入：nums = [100,4,200,1,3,2]    输出：4
# 输入：nums = [0,3,7,2,5,8,4,6,0,1] 输出：9

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # num_set = set(nums)
        # ans = 0

        # for num in num_set:
        #     if num - 1 in num_set:
        #         continue

        #     current = num
        #     length = 1
        #     while current + 1 in num_set:
        #         current += 1
        #         length += 1

        #     ans = max(ans, length)

        # return ans
        num_set = set(nums)
        ans = 0

        for i, num in nums:
            if num - 1 not in num_set:
                continue
            curr = num + 1
            len = 1
            while curr in nums:
                curr += 1
                len += 1
            ans = max(ans, len)
        return ans
    
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for n in nums:
            if n - 1 not in num_set:
                curr = n + 1
                len = 1
                while curr in num_set:
                    curr += 1
                    len += 1    # **注意长度增加**
                ans = max(len, ans)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))         # 4
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
