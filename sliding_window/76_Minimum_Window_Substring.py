# 76. 最小覆盖子串
# https://leetcode.cn/problems/minimum-window-substring/
# 难度：困难
#
# 给你一个字符串 s、一个字符串 t。返回 s 中涵盖 t 所有字符的最小子串。
# 如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 ""。
#
# 示例：
# 输入：s = "ADOBECODEBANC", t = "ABC"  输出："BANC"
# 输入：s = "a", t = "a"                输出："a"
# 输入：s = "a", t = "aa"               输出：""
#
# 思路：可变滑动窗口。
# 右指针扩张直到窗口覆盖 t，覆盖后左指针收缩，尝试缩短答案。

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        # remain 表示还有多少种字符没有满足数量要求。
        remain = len(need)

        left = 0
        ans_start = 0
        ans_len = float("inf")

        for right, ch in enumerate(s):
            # 右侧字符进入窗口，如果是需要的字符，就减少需求量。
            if ch in need:
                need[ch] -= 1
                if need[ch] == 0:
                    remain -= 1

            # remain == 0 表示当前窗口已经覆盖 t，开始尝试收缩左边界。
            while remain == 0:
                if right - left + 1 < ans_len:
                    ans_start = left
                    ans_len = right - left + 1

                left_ch = s[left]
                left += 1

                # 左侧字符出窗口。如果移走后数量不够，窗口重新变为不满足。
                if left_ch in need:
                    need[left_ch] += 1
                    if need[left_ch] > 0:
                        remain += 1

        return "" if ans_len == float("inf") else s[ans_start:ans_start + ans_len]


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))  # BANC
    print(s.minWindow("a", "a"))                # a
    print(s.minWindow("a", "aa"))               # ""

