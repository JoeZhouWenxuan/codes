# 5. 最长回文子串
# https://leetcode.cn/problems/longest-palindromic-substring/
# 难度：中等
#
# 给你一个字符串 s，找到 s 中最长的回文子串。
#
# 示例：
# 输入：s = "babad"  输出："bab"（或 "aba"）
# 输入：s = "cbbd"   输出："bb"


# ── 方法一：中心扩展法 O(n²) 时间，O(1) 空间 ──────────────────────────────
class SolutionExpand:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 退出时 s[left+1..right-1] 是回文
            return s[left + 1:right]

        res = ""
        for i in range(len(s)):
            odd  = expand(i, i)      # 奇数长度，以 s[i] 为中心
            even = expand(i, i + 1)  # 偶数长度，以 s[i..i+1] 为中心
            if len(odd)  > len(res): res = odd
            if len(even) > len(res): res = even
        return res


# ── 方法二：Manacher 算法 O(n) 时间，O(n) 空间 ────────────────────────────
#
# 核心思想：
#   1. 预处理：在字符间插入 '#'，统一奇偶回文。
#      "abba" → "#a#b#b#a#"
#   2. 维护当前最右回文边界 r 及其中心 c，p[i] 记录 i 处的回文半径。
#   3. 对每个新位置 i：
#      - 若 i < r，镜像位置 mirror = 2c - i 已算过，
#        可直接初始化 p[i] = min(p[mirror], r - i)，跳过已知部分。
#      - 再从 p[i] 出发继续向外扩展（最多扩展常数次均摊）。
#   4. 全程每个位置最多被"右边界"扫过一次，整体 O(n)。
#
# 回文半径 → 原始字符串中的位置换算：
#   新串中心 i，半径 p[i]  →  原始串起点 (i - p[i]) // 2，长度 p[i]
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # # 预处理
        # t = '#' + '#'.join(s) + '#'
        # n = len(t)
        # p = [0] * n   # p[i]：t[i] 为中心的回文半径（不含自身）
        # c = r = 0     # c：最右回文的中心；r：最右回文的右边界（开区间）

        # for i in range(n):
        #     if i < r:
        #         mirror = 2 * c - i
        #         p[i] = min(p[mirror], r - i)   # 利用镜像初始化，避免重复计算

        #     # 从已知边界继续扩展
        #     left, right = i - (p[i] + 1), i + (p[i] + 1)
        #     while left >= 0 and right < n and t[left] == t[right]:
        #         p[i] += 1
        #         left  -= 1
        #         right += 1

        #     # 更新最右边界
        #     if i + p[i] > r:
        #         c, r = i, i + p[i]

        # # 找最大半径，还原到原始串
        # max_i = p.index(max(p))
        # start = (max_i - p[max_i]) // 2
        # return s[start: start + p[max_i]]
        t = "#" + "#".join(s) + "#"
        n = len(t)
        p = [0] * n
        c, r = 0, 0
        for i in range(n):
            if i < r:
                mirror = 2*c - i
                p[i] = min(p[mirror], r - i)
            left, right = i - (p[i]+1), i + (p[i]+1)
            while left >= 0 and right < n and t[left] == t[right]:
                p[i] += 1
                left -= 1
                right += 1
            if i + p[i] > r:
                c, r = i, i+p[i]
        max_i = p.index(max(p))
        start = (max_i - p[max_i]) // 2
        return s[start, start+p[max_i]]
            

if __name__ == "__main__":
    expand   = SolutionExpand()
    manacher = Solution()

    cases = ["babad", "cbbd", "a", "racecar", "aacabdkacaa"]
    for c in cases:
        r1 = expand.longestPalindrome(c)
        r2 = manacher.longestPalindrome(c)
        print(f"{c!r:20s}  expand={r1!r:12s}  manacher={r2!r}")
