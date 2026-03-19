# 20. 有效的括号
# https://leetcode.cn/problems/valid-parentheses/
# 难度：简单
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s，判断字符串是否有效。
# 有效字符串需满足：
#   1. 左括号必须用相同类型的右括号闭合。
#   2. 左括号必须以正确的顺序闭合。
#   3. 每个右括号都有一个对应的相同类型的左括号。
#
# 示例：
# 输入：s = "()"      输出：true
# 输入：s = "()[]{}"  输出：true
# 输入：s = "(]"      输出：false
#
# 思路：栈，遇到左括号入栈，遇到右括号检查栈顶是否匹配。

class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s:
            if ch in match:
                if not stack or stack[-1] != match[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))      # True
    print(s.isValid("()[]{}"))  # True
    print(s.isValid("(]"))      # False
    print(s.isValid("([)]"))    # False
    print(s.isValid("{[]}"))    # True
