# 409. 最长回文串
# https://leetcode.cn/problems/longest-palindrome/
# 难度：简单
#
# 给定一个包含大小写字母的字符串 s，返回通过这些字母构造成的最长回文串的长度。
#
# 示例：
# 输入：s = "abccccdd"    输出：7
# 输入：s = "a"           输出：1

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        ans = 0
        odd_found = False

        for count in counts.values():
            ans += (count // 2) * 2
            if count % 2 == 1:
                odd_found = True

        return ans + 1 if odd_found else ans


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))  # 7
    print(s.longestPalindrome("a"))         # 1
