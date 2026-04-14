# 136. 只出现一次的数字
# https://leetcode.cn/problems/single-number/
# 难度：简单
#
# 给你一个非空整数数组 nums，除了某个元素只出现一次以外，其余每个元素均出现两次。
# 找出那个只出现了一次的元素。
#
# 示例：
# 输入：nums = [2,2,1]    输出：1
# 输入：nums = [4,1,2,1,2] 输出：4

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ans = 0
        # for num in nums:
        #     ans ^= num
        # return ans
        ans = 0
        for num in nums:
            ans ^= num

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2, 2, 1]))     # 1
    print(s.singleNumber([4, 1, 2, 1, 2]))  # 4
