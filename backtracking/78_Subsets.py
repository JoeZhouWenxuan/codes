# 78. 子集
# https://leetcode.cn/problems/subsets/
# 难度：中等
#
# 给你一个整数数组 nums，数组中的元素互不相同。返回该数组所有可能的子集。
#
# 示例：
# 输入：nums = [1,2,3]    输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 输入：nums = [0]        输出：[[],[0]]

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # ans = []
        # path = []

        # def backtrack(start: int) -> None:
        #     ans.append(path[:])
        #     for i in range(start, len(nums)):
        #         path.append(nums[i])
        #         backtrack(i + 1)
        #         path.pop()

        # backtrack(0)
        # return ans
        ans = []
        path = []
        def dfs(index):
            ans.append(path[:])
            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(i+1)
                path.pop()
        dfs(0)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))
    print(s.subsets([0]))
