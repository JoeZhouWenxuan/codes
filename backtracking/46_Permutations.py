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
        # path 保存当前正在构造的一条排列。
        path = []
        # used[i] 表示 nums[i] 是否已经被放入当前 path，避免同一个位置的元素重复使用。
        used = [False] * len(nums)

        def dfs():
            # 当前排列长度等于 nums 长度，说明已经选完所有数字，记录一份结果。
            if len(path) == len(nums):
                ans.append(path[:])
                return

            # 每一层都从所有数字中尝试选择一个还没用过的数字。
            for i, num in enumerate(nums):
                if not used[i]:
                    path.append(num)
                    used[i] = True
                    dfs()
                    # 回溯：撤销本层选择，恢复现场，继续尝试下一个数字。
                    used[i] = False
                    path.pop()

        dfs()
        return ans
    
        ans = []
        path = []
        visited = [False] * len(nums)
        def dfs():
            if len(path) == len(nums):
                ans.append(path[: ])
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                path.append(nums[i])
                visited[i] = True
                dfs()
                visited[i] = False
                path.pop()
        dfs()
        return ans
    
    def permuteUnique(nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        path = []
        used = [False] * len(nums)

        def dfs():
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i, num in enumerate(nums):
                if used[i]:
                    continue

                # 同一层中，如果前一个相同数字还没被使用，
                # 说明当前 num 会产生重复排列，跳过。
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(num)
                dfs()
                path.pop()
                used[i] = False

        dfs()
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))
    print(s.permute([0, 1]))
