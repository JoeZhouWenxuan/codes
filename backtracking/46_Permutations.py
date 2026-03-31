# 46. 全排列
# https://leetcode.cn/problems/permutations/
# 难度：中等
#
# 给定一个不含重复数字的数组 nums，返回其所有可能的全排列。
#
# 示例：
# 输入：nums = [1,2,3]    输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 输入：nums = [0,1]      输出：[[0,1],[1,0]]

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # ans = []
        # path = []
        # used = [False] * len(nums)

        # def backtrack() -> None:
        #     if len(path) == len(nums):
        #         ans.append(path[:])
        #         return

        #     for i, num in enumerate(nums):
        #         if used[i]:
        #             continue
        #         used[i] = True
        #         path.append(num)
        #         backtrack()
        #         path.pop()
        #         used[i] = False

        # backtrack()
        # return ans

        ans = []
        n = len(nums)
        used = [False] * n
        path = []
        def dfs():
            if len(path) == n:
                ans.append(path[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                dfs()
                path.pop()
                used[i] = False

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))
    print(s.permute([0, 1]))
