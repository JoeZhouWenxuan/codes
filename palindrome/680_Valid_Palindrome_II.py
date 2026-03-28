# 680. 验证回文串 II
# https://leetcode.cn/problems/valid-palindrome-ii/
# 难度：简单
#
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文串。
#
# 示例：
# 输入：s = "aba"    输出：True
# 输入：s = "abca"   输出：True


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_pal(left + 1, right) or is_pal(left, right - 1)
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.validPalindrome("aba"))   # True
    print(s.validPalindrome("abca"))  # True
