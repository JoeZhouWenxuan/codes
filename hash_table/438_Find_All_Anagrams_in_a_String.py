# 438. 找到字符串中所有字母异位词
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/
# 难度：中等
#
# 给定两个字符串 s 和 p，找到 s 中所有 p 的异位词的子串，返回这些子串的起始索引。
#
# 示例：
# 输入：s = "cbaebabacd", p = "abc"    输出：[0,6]
# 输入：s = "abab", p = "ab"           输出：[0,1,2]

from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        window = Counter()
        left = 0
        ans = []

        for right, ch in enumerate(s):
            window[ch] += 1

            if right - left + 1 > len(p):
                left_char = s[left]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                left += 1

            if window == need:
                ans.append(left)

        return ans
    
    def findAnagrams2(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        window = Counter()
        ans = []
        left = 0
        for right, x in enumerate(s):
            if x not in need:
                window.clear()
                left = right + 1
                continue
            window[x] += 1

            while window[x] > need[x]:
                left_char = s[left]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                left += 1

            if right - left + 1 == len(p):
                ans.append(left)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))  # [0, 6]
    print(s.findAnagrams2("cbaebabacd", "abc"))  # [0, 6]
    print(s.findAnagrams("abab", "ab"))         # [0, 1, 2]
    print(s.findAnagrams2("abab", "ab"))         # [0, 1, 2]
