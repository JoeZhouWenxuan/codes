# 242. 有效的字母异位词
# https://leetcode.cn/problems/valid-anagram/
# 难度：简单
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例：
# 输入：s = "anagram", t = "nagaram"    输出：True
# 输入：s = "rat", t = "car"            输出：False

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))  # True
    print(s.isAnagram("rat", "car"))          # False
