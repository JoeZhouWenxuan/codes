# 5. 最长回文子串
# https://leetcode.cn/problems/longest-palindromic-substring/
# 难度：中等
#
# 给你一个字符串 s，找到 s 中最长的回文子串。
#
# 示例：
# 输入：s = "babad"  输出："bab"（或 "aba"）
# 输入：s = "cbbd"   输出："bb"
#
# 思路：中心扩展法，以每个字符（奇数长度）和每两个相邻字符（偶数长度）为中心向外扩展。

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 退出时 s[left+1..right-1] 是回文
            return s[left + 1:right]

        res = ""
        for i in range(len(s)):
            odd = expand(i, i)       # 奇数长度，以 s[i] 为中心
            even = expand(i, i + 1)  # 偶数长度，以 s[i..i+1] 为中心
            if len(odd) > len(res):
                res = odd
            if len(even) > len(res):
                res = even

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))   # "bab" 或 "aba"
    print(s.longestPalindrome("cbbd"))    # "bb"
    print(s.longestPalindrome("a"))       # "a"
    print(s.longestPalindrome("racecar")) # "racecar"
