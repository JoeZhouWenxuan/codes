# 131. 分割回文串
# https://leetcode.cn/problems/palindrome-partitioning/
# 难度：中等
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。返回 s 所有可能的分割方案。
#
# 示例：
# 输入：s = "aab"    输出：[["a","a","b"],["aa","b"]]
# 输入：s = "a"      输出：[["a"]]

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # ans = []
        # path = []

        # def is_palindrome(sub: str) -> bool:
        #     return sub == sub[::-1]

        # def backtrack(start: int) -> None:
        #     if start == len(s):
        #         ans.append(path[:])
        #         return

        #     for end in range(start + 1, len(s) + 1):
        #         sub = s[start:end]
        #         if not is_palindrome(sub):
        #             continue
        #         path.append(sub)
        #         backtrack(end)
        #         path.pop()

        # backtrack(0)
        # return ans

        ans = []
        path = []
        def is_palindrome(s):
            return s == s[::-1]
        
        def dfs(index):
            # if index == len(s):
            #     ans.append(path[:])
            #     return
            # for j in range(index+1, len(s) + 1):
            #     sub = s[index, j]
            #     if not is_palindrome(sub):
            #         continue
            #     path.append(sub)
            #     dfs(j)
            #     path.pop()
            if index == len(s):
                ans.append(path[:])
                return
            for i in range(index + 1, len(s) + 1):
                sub_str = s[index: i]
                if not is_palindrome(sub_str):
                    continue
                path.append(sub_str)
                dfs(i)  # 注意是i，因为sub_str是左闭右开
                path.pop()
        dfs(0)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))
    print(s.partition("a"))
