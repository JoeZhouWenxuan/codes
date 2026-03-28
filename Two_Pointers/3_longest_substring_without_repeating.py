# 3. 无重复字符的最长子串
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/
# 难度：中等
#
# 给定一个字符串 s，请你找出其中不含有重复字符的最长子串的长度。
#
# 示例：
# 输入：s = "abcabcbb"  输出：3  ("abc")
# 输入：s = "bbbbb"     输出：1  ("b")
# 输入：s = "pwwkew"   输出：3  ("wke")
#
# 思路：滑动窗口 + 哈希集合，右指针扩张，遇到重复时左指针收缩。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        ans = 0

        for right, ch in enumerate(s):
            while ch in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(ch)
            ans = max(ans, right - left + 1)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(s.lengthOfLongestSubstring("bbbbb"))     # 1
    print(s.lengthOfLongestSubstring("pwwkew"))    # 3
    print(s.lengthOfLongestSubstring(""))          # 0
