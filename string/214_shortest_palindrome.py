# 214. 最短回文串
# https://leetcode.cn/problems/shortest-palindrome/
# 难度：困难
#
# 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。
# 返回可以用这种方式转换的最短回文串。
#
# 示例：
# 输入：s = "aacecaaa"    输出："aaacecaaa"
# 输入：s = "abcd"        输出："dcbabcd"


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        combined = s + "#" + rev
        lps = [0] * len(combined)

        for i in range(1, len(combined)):
            length = lps[i - 1]
            while length > 0 and combined[i] != combined[length]:
                length = lps[length - 1]
            if combined[i] == combined[length]:
                length += 1
            lps[i] = length

        longest_prefix = lps[-1]
        return rev[: len(s) - longest_prefix] + s


if __name__ == "__main__":
    s = Solution()
    print(s.shortestPalindrome("aacecaaa"))  # aaacecaaa
    print(s.shortestPalindrome("abcd"))      # dcbabcd
