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

    def lengthOfLongestSubstring2(self, s: str) -> int:
        last_seen = {}
        ans = 0
        left = 0

        for i, x in enumerate(s):
            '''
            举个最典型的例子：abba
                我们一步一步看：

                i = 0, x = 'a'

                last_seen 里没有 a
                窗口是 "a"
                left = 0
                i = 1, x = 'b'

                last_seen 里没有 b
                窗口是 "ab"
                left = 0
                i = 2, x = 'b'

                b in last_seen，而且 last_seen['b'] = 1 >= left(0)
                说明这个旧的 b 还在当前窗口 "ab" 里
                所以要把 left 移到 1 + 1 = 2
                新窗口变成 "b"
                i = 3, x = 'a'

                a in last_seen，last_seen['a'] = 0
                但这时 left = 2
                所以 0 >= 2 不成立

            '''
            if x in last_seen and last_seen[x] >= left: # 举个例子
                left = last_seen[x] + 1
            last_seen[x] = i
            ans = max(ans, i - left + 1)

        return ans
    
    def f(self, s):
        last_seen = {}
        left = 0
        ans = 0
        for right, ch in enumerate(s):

            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(s.lengthOfLongestSubstring("bbbbb"))     # 1
    print(s.lengthOfLongestSubstring("pwwkew"))    # 3
    print(s.lengthOfLongestSubstring(""))          # 0
