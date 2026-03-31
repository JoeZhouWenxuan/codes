# 301. 删除无效的括号
# https://leetcode.cn/problems/remove-invalid-parentheses/
# 难度：困难
#
# 给你一个由若干括号和字母组成的字符串 s，删除最小数量的无效括号，使得输入的字符串有效。
# 返回所有可能的结果。
#
# 示例：
# 输入：s = "()())()"    输出：["(())()","()()()"]
# 输入：s = "(a)())()"   输出：["(a())()","(a)()()"]

from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # left_remove = right_remove = 0
        # for ch in s:
        #     if ch == "(":
        #         left_remove += 1
        #     elif ch == ")":
        #         if left_remove > 0:
        #             left_remove -= 1
        #         else:
        #             right_remove += 1

        # ans = set()

        # def backtrack(index: int, left_count: int, right_count: int, left_remove: int, right_remove: int, path: List[str]) -> None:
        #     if index == len(s):
        #         if left_remove == 0 and right_remove == 0:
        #             ans.add("".join(path))
        #         return

        #     ch = s[index]

        #     if ch == "(" and left_remove > 0:
        #         backtrack(index + 1, left_count, right_count, left_remove - 1, right_remove, path)
        #     if ch == ")" and right_remove > 0:
        #         backtrack(index + 1, left_count, right_count, left_remove, right_remove - 1, path)

        #     path.append(ch)

        #     if ch not in "()":
        #         backtrack(index + 1, left_count, right_count, left_remove, right_remove, path)
        #     elif ch == "(":
        #         backtrack(index + 1, left_count + 1, right_count, left_remove, right_remove, path)
        #     elif right_count < left_count:
        #         backtrack(index + 1, left_count, right_count + 1, left_remove, right_remove, path)

        #     path.pop()

        # backtrack(0, 0, 0, left_remove, right_remove, [])
        # return list(ans)
        lremove, rremove = 0, 0
        for ch in s:
            if ch == '(':
                lremove += 1
            elif ch == ')':
                if lremove > 0:
                    lremove -= 1
                else:
                    rremove += 1
        
        path = []
        ans = set()
        def dfs(index, lremove, rremove, lcount, rcount):
            if index == len(s):
                if lremove == 0 and rremove == 0:
                    ans.add("".join(path))
                return
            
            ch = s[index]
            if ch == '(' and lremove > 0:
                dfs(index + 1, lremove - 1, rremove, lcount, rcount)
            if ch == ')' and rremove > 0:
                dfs(index + 1, lremove, rremove - 1, lcount, rcount)

            path.append(ch)
            if ch not in "()":
                dfs(index + 1, lremove, rremove, lcount, rcount)
            elif ch == "(":
                dfs(index + 1, lremove, rremove, lcount+1, rcount)
            elif rcount < lcount:
                dfs(index + 1, lremove, rremove, lcount, rcount + 1)
            path.pop()
        dfs(0, lremove, rremove, 0, 0)
        return list(ans)


if __name__ == "__main__":
    s = Solution()
    print(sorted(s.removeInvalidParentheses("()())()")))   # ['(())()', '()()()']
    print(sorted(s.removeInvalidParentheses("(a)())()")))  # ['(a())()', '(a)()()']
    print(sorted(s.removeInvalidParentheses(")("))) 
