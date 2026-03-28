# 32. 最长有效括号
# https://leetcode.cn/problems/longest-valid-parentheses/
# 难度：困难
#
# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
#
# 示例：
# 输入：s = "(()"     输出：2  （最长有效括号子串是 "()"）
# 输入：s = ")()())"  输出：4  （最长有效括号子串是 "()()"）
# 输入：s = ""        输出：0
#
# 思路：栈，存储字符索引。
# 栈底始终维护"最后一个未匹配的右括号索引"作为基准。
# 遇到 '(' 入栈；遇到 ')' 出栈，栈空时将当前索引入栈（新基准），
# 否则用当前索引减去栈顶索引得到有效长度。

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # 初始基准索引
        ans = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # 当前 ')' 成为新基准
                else:
                    ans = max(ans, i - stack[-1])

        return ans
    
    def f(self, s: str) -> int:
        stack = [-1]
        ans = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop() # 因为这里pop操作，所以stack初始-1这个值
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans




if __name__ == "__main__":
    s = Solution()
    print(s.longestValidParentheses("(()"))    # 2
    print(s.longestValidParentheses(")()())")) # 4
    print(s.longestValidParentheses(""))       # 0
    print(s.longestValidParentheses("()(()))))(()"))  # 6
