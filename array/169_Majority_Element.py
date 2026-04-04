# 169. 多数元素
# https://leetcode.cn/problems/majority-element/
# 难度：简单
#
# 给定一个大小为 n 的数组 nums，返回其中的多数元素。多数元素是指在数组中出现次数大于 n / 2 的元素。
#
# 示例：
# 输入：nums = [3,2,3]    输出：3
# 输入：nums = [2,2,1,1,1,2,2]    输出：2

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # candidate = None
        # count = 0

        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #     count += 1 if num == candidate else -1

        # return candidate
        '''
        candidate
        表示：
        当前我们认为“可能是多数元素”的候选人
        count
        表示：
        当前候选人相对于其他数的“净胜票数”
        '''
        candidate = None
        count = 0
        for num in nums:
            '''
            如果当前没有候选人了，就把当前数设为候选人
            如果新来的数和候选人一样，票数 +1
            不一样，票数 -1
            '''
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3, 2, 3]))              # 3
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
