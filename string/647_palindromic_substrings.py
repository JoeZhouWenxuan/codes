# 647. 回文子串
# https://leetcode.cn/problems/palindromic-substrings/
# 难度：中等
#
# 给你一个字符串 s，请你统计并返回这个字符串中回文子串的数目。
#
# 示例：
# 输入：s = "abc"   输出：3
# 输入：s = "aaa"   输出：6
#
# 思路：
# 1. 中心扩展：以每个位置和相邻空隙为中心向两边扩展
# 2. 动态规划：dp[i][j] 表示 s[i..j] 是否为回文
# 3. Manacher：线性时间统计所有回文半径


class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        ans = 0
        for i in range(len(s)):
            ans += expand(i, i)
            ans += expand(i, i + 1)

        return ans


class Solution2:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    ans += 1

        return ans


class Solution3:
    def countSubstrings(self, s: str) -> int:
        t = "#" + "#".join(s) + "#"
        n = len(t)
        p = [0] * n
        center = right = 0
        ans = 0

        for i in range(n):
            if i < right:
                mirror = 2 * center - i
                p[i] = min(p[mirror], right - i)

            while (
                i - p[i] - 1 >= 0
                and i + p[i] + 1 < n
                and t[i - p[i] - 1] == t[i + p[i] + 1]
            ):
                p[i] += 1

            if i + p[i] > right:
                center, right = i, i + p[i]

            ans += (p[i] + 1) // 2

        return ans


if __name__ == "__main__":
    cases = [("abc", 3), ("aaa", 6), ("aba", 4)]

    for Cls in [Solution, Solution2, Solution3]:
        solver = Cls()
        print(Cls.__name__)
        for text, expected in cases:
            result = solver.countSubstrings(text)
            status = "OK" if result == expected else f"FAIL (got {result})"
            print(f"  {text!r} -> {result}  {status}")
