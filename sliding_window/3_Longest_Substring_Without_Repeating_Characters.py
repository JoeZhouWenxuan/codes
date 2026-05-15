# 3. 无重复字符的最长子串
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/
# 难度：中等
#
# 给定一个字符串 s，请你找出其中不含有重复字符的最长子串的长度。
#
# 示例：
# 输入：s = "abcabcbb"  输出：3
# 输入：s = "bbbbb"     输出：1
# 输入：s = "pwwkew"    输出：3
#
# 思路：滑动窗口 + 哈希表。
# left 表示当前无重复窗口的左边界，right 表示右边界。
# last_seen[ch] 记录字符 ch 上一次出现的位置。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        ans = 0

        for right, ch in enumerate(s):
            # 如果 ch 上一次出现的位置还在当前窗口里，说明出现重复。
            # left 直接跳到上一次 ch 的下一个位置。
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1

            # 更新 ch 最近一次出现的位置。
            last_seen[ch] = right
            # 当前窗口 [left, right] 一定没有重复字符。
            ans = max(ans, right - left + 1)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(s.lengthOfLongestSubstring("bbbbb"))     # 1
    print(s.lengthOfLongestSubstring("pwwkew"))    # 3
    print(s.lengthOfLongestSubstring(""))          # 0

