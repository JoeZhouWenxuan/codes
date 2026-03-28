# 5. 最长回文子串
# https://leetcode.cn/problems/longest-palindromic-substring/
# 难度：中等
#
# 给你一个字符串 s，找到 s 中最长的回文子串。
#
# 示例：
# 输入：s = "babad"  输出："bab"（或 "aba"）
# 输入：s = "cbbd"   输出："bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        ans = ""
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)
            if len(odd) > len(ans):
                ans = odd
            if len(even) > len(ans):
                ans = even

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))  # bab / aba
    print(s.longestPalindrome("cbbd"))   # bb
