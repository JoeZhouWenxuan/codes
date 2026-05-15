# 77. 组合
# https://leetcode.cn/problems/combinations/
# 难度：中等
#
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
# 示例：
# 输入：n = 4, k = 2    输出：[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# 输入：n = 1, k = 1    输出：[[1]]

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(start: int) -> None:
            if len(path) == k:
                ans.append(path[:])
                return

            for num in range(start, n + 1):
                path.append(num)
                backtrack(num + 1)
                path.pop()

        backtrack(1)
        return ans
    
        # ans = []
        # path = []

        # def dfs(start):
        #     if len(path) == k:
        #         ans.append(path[:])
        #         return
            
        #     for i in range(start, n + 1):
        #         path.append(i)
        #         dfs(i + 1)
        #         path.pop()
        # dfs(1)
        # return ans


if __name__ == "__main__":
    s = Solution()
    print(s.combine(4, 2))  # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    print(s.combine(1, 1))  # [[1]]
