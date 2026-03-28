# 9. 回文数
# https://leetcode.cn/problems/palindrome-number/
# 难度：简单
#
# 给你一个整数 x，如果 x 是一个回文整数，返回 true；否则，返回 false。
#
# 示例：
# 输入：x = 121    输出：True
# 输入：x = -121   输出：False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))   # True
    print(s.isPalindrome(-121))  # False
