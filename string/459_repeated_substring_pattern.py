# 459. 重复的子字符串
# https://leetcode.cn/problems/repeated-substring-pattern/
# 难度：简单（核心考点：KMP next 数组性质）
#
# 给定一个非空字符串 s，判断它是否可以由它的一个子串重复若干次构成。
#
# 示例：
# "abab"   → True  （"ab" 重复 2 次）
# "aba"    → False
# "abcabc" → True  （"abc" 重复 2 次）


# ── 方法一：拼接判断 O(n) ────────────────────────────────────────────────────
#
# 将 s+s 的首尾各去掉一个字符，若 s 仍是子串，则 s 由重复子串构成。
# 原理：若 s = k * t，则 s+s = 2k * t，去掉首尾字符后仍包含完整的 s。
class SolutionConcat:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]


# ── 方法二：KMP next 数组性质 O(n) ──────────────────────────────────────────
#
# 结论：s 由重复子串构成 ⟺ next[n-1] != 0 且 n % (n - next[n-1]) == 0
#
# 推导：
#   设 next[n-1] = k，则 s[0..k-1] == s[n-k..n-1]（长为 k 的前缀 = 后缀）
#   令最小重复单元长度 d = n - k
#   若 n % d == 0，说明整个字符串可由长为 d 的子串重复 n/d 次构成。
#
# 示例：s = "abcabc"  n=6
#   next = [0, 0, 0, 1, 2, 3]
#   next[5] = 3，d = 6 - 3 = 3，6 % 3 == 0 → True，重复单元 "abc"
#
# 示例：s = "abab"  n=4
#   next = [0, 0, 1, 2]
#   next[3] = 2，d = 4 - 2 = 2，4 % 2 == 0 → True，重复单元 "ab"
#
# 示例：s = "aba"  n=3
#   next = [0, 0, 1]
#   next[2] = 1，d = 3 - 1 = 2，3 % 2 != 0 → False

def build_next(p: str) -> list:
    n = len(p)
    next_ = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and p[i] != p[j]:
            j = next_[j - 1]
        if p[i] == p[j]:
            j += 1
        next_[i] = j
    return next_

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        next_ = build_next(s)
        k = next_[n - 1]           # 最长公共前后缀长度
        d = n - k                  # 候选最小重复单元长度
        return k != 0 and n % d == 0


if __name__ == "__main__":
    sol1 = SolutionConcat()
    sol2 = Solution()

    cases = [
        ("abab",   True),
        ("aba",    False),
        ("abcabc", True),
        ("abcabcabcabc", True),
        ("a",      False),
        ("aa",     True),
    ]
    for s, expected in cases:
        r1 = sol1.repeatedSubstringPattern(s)
        r2 = sol2.repeatedSubstringPattern(s)
        status = "✓" if r1 == r2 == expected else "✗"
        print(f"{status} {s!r:20s}  concat={r1}  kmp={r2}  expected={expected}")
