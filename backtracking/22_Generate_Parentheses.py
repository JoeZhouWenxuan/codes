# 22. 括号生成
# https://leetcode.cn/problems/generate-parentheses/
# 难度：中等
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。
#
# 示例：
# 输入：n = 3    输出：["((()))","(()())","(())()","()(())","()()()"]
# 输入：n = 1    输出：["()"]

from typing import List


class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:
    #     ans = []
    #     path = []

    #     def backtrack(left: int, right: int) -> None:
    #         if len(path) == 2 * n:
    #             ans.append("".join(path))
    #             return

    #         if left < n:
    #             path.append("(")
    #             backtrack(left + 1, right)
    #             path.pop()

    #         if right < left:
    #             path.append(")")
    #             backtrack(left, right + 1)
    #             path.pop()

    #     backtrack(0, 0)
    #     return ans
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = []
        def dfs(left, right):
            if len(path) == 2 * n:
                ans.append("".join(path[:]))
                return
            if left < n:
                path.append("(")
                dfs(left + 1, right)
                path.pop()
            elif right < left:
                path.append(")")
                dfs(left, right + 1)
                path.pop()
        dfs(0, 0)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
    print(s.generateParenthesis(1))
