# 438. 找到字符串中所有字母异位词
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/
# 难度：中等
#
# 给定两个字符串 s 和 p，找到 s 中所有 p 的异位词的子串，返回这些子串的起始索引。
# 答案以任意顺序返回。
#
# 示例：
# 输入：s = "cbaebabacd", p = "abc"  输出：[0,6]
# 输入：s = "abab", p = "ab"         输出：[0,1,2]
#
# 思路：固定大小滑动窗口（窗口长度 = len(p)），用计数器比较。
# 维护 need（p 的字符需求）和 remain（未满足的字符种数），O(n) 时间。

from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        need = Counter(p)
        remain = len(need)   # 需要满足的字符种数
        ans = []
        left = 0

        for right, ch in enumerate(s):
            if ch in need:
                need[ch] -= 1
                if need[ch] == 0:
                    remain -= 1

            # 窗口超出 p 的长度，收缩左边界
            if right - left + 1 > len(p):
                left_ch = s[left]
                left += 1
                if left_ch in need:
                    if need[left_ch] == 0:
                        remain += 1
                    need[left_ch] += 1

            if remain == 0:
                ans.append(left)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))  # [0, 6]
    print(s.findAnagrams("abab", "ab"))          # [0, 1, 2]
