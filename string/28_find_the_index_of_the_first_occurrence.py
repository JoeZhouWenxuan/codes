# 28. 找出字符串中第一个匹配项的下标
# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/
# 难度：简单（核心考点：KMP）
#
# 给你两个字符串 haystack 和 needle，在 haystack 中找出 needle 第一次出现的下标，
# 不存在则返回 -1。


# ── KMP 核心：构建 next 数组 ────────────────────────────────────────────────
#
# next[i] = 模式串 p[0..i] 中，最长的「既是前缀又是后缀」的子串长度。
#
# 示例：p = "aabaa"
#   i=0  'a'        next[0] = 0  （单字符无proper前后缀）
#   i=1  'aa'       next[1] = 1  （前缀"a" == 后缀"a"）
#   i=2  'aab'      next[2] = 0  （无公共前后缀）
#   i=3  'aaba'     next[3] = 1  （前缀"a" == 后缀"a"）
#   i=4  'aabaa'    next[4] = 2  （前缀"aa" == 后缀"aa"）
#
# 构建过程（双指针）：
#   - j 指向「当前前缀的末尾」，也代表已匹配长度
#   - i 从 1 开始遍历
#   - p[i] == p[j]：都右移，next[i] = j+1
#   - p[i] != p[j] 且 j>0：j 回退到 next[j-1]（利用已有结果，不从头开始）
#   - p[i] != p[j] 且 j==0：next[i] = 0

def build_next(p: str) -> list:
    n = len(p)
    next_ = [0] * n
    j = 0                       # j：前缀指针，也表示当前最长公共前后缀长度
    for i in range(1, n):
        while j > 0 and p[i] != p[j]:
            j = next_[j - 1]   # 失配：利用已有 next 值回退，而非归零
        if p[i] == p[j]:
            j += 1
        next_[i] = j
    return next_


# ── KMP 匹配 ────────────────────────────────────────────────────────────────
#
# 主串指针 i 永不回退，模式串指针 j 在失配时通过 next 跳转。
#
# 关键：失配时 j = next[j-1]，表示「已匹配的前缀中，最长的既是前缀又是后缀
#       的部分」仍然有效，直接从那里继续比较，避免重复计算。
#
#   haystack = "aabaabaaf"
#   needle   = "aabaa"   next = [0,1,0,1,2]
#
#   i=0..4 匹配成功 j=5，未满足返回条件，继续
#   i=5 'b' vs p[2]='b' → 匹配
#   i=6 'a' vs p[3]='a' → 匹配
#   i=7 'a' vs p[4]='a' → 匹配，j=5 == len(needle)，返回 i-j+1 = 3

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0

        next_ = build_next(needle)
        j = 0                           # 模式串指针
        for i in range(m):              # 主串指针（永不回退）
            while j > 0 and haystack[i] != needle[j]:
                j = next_[j - 1]       # 失配：j 跳转，i 不动
            if haystack[i] == needle[j]:
                j += 1
            if j == n:                  # 匹配完成
                return i - n + 1
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.strStr("sadbutsad", "sad"))   # 0
    print(s.strStr("leetcode", "leeto"))  # -1
    print(s.strStr("aabaabaaf", "aabaa")) # 0
    print(s.strStr("aaa", "aa"))          # 0
    print(s.strStr("a", "a"))             # 0
