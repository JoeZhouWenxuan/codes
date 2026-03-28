# 383. 赎金信
# https://leetcode.cn/problems/ransom-note/
# 难度：简单
#
# 给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
#
# 示例：
# 输入：ransomNote = "a", magazine = "b"    输出：False
# 输入：ransomNote = "aa", magazine = "aab" 输出：True

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        need = Counter(ransomNote)
        supply = Counter(magazine)
        return all(supply[ch] >= count for ch, count in need.items())


if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct("a", "b"))    # False
    print(s.canConstruct("aa", "aab"))  # True
