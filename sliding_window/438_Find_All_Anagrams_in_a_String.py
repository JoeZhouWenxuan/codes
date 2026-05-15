# 438. 找到字符串中所有字母异位词
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/
# 难度：中等
#
# 给定两个字符串 s 和 p，找到 s 中所有 p 的异位词的子串，返回这些子串的起始索引。
#
# 示例：
# 输入：s = "cbaebabacd", p = "abc"    输出：[0, 6]
# 输入：s = "abab", p = "ab"           输出：[0, 1, 2]
#
# 思路：固定长度滑动窗口。
# 异位词长度一定等于 len(p)，所以窗口长度固定为 len(p)。

from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        window = Counter()
        left = 0
        ans = []

        for right, ch in enumerate(s):
            # 右侧字符进入窗口。
            window[ch] += 1

            # 窗口长度超过 len(p) 时，左侧字符出窗口。
            if right - left + 1 > len(p):
                left_ch = s[left]
                window[left_ch] -= 1
                if window[left_ch] == 0:
                    del window[left_ch]
                left += 1

            # 窗口长度固定后，如果字符计数完全相同，就是一个异位词。
            if window == need:
                ans.append(left)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))  # [0, 6]
    print(s.findAnagrams("abab", "ab"))         # [0, 1, 2]

