# 647. 回文子串
# https://leetcode.cn/problems/palindromic-substrings/
# 难度：中等
#
# 给你一个字符串 s，请你统计并返回这个字符串中回文子串的数目。
#
# 示例：
# 输入：s = "abc"   输出：3
# 输入：s = "aaa"   输出：6


class Solution:
    def countSubstrings(self, s: str) -> int:
        # def expand(left: int, right: int) -> int:
        #     count = 0
        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         count += 1
        #         left -= 1
        #         right += 1
        #     return count

        # ans = 0
        # for i in range(len(s)):
        #     ans += expand(i, i)
        #     ans += expand(i, i + 1)

        # return ans
        def expand(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        
        ans = 0
        for i in range(len(s)):
            ans += expand(i, i)
            ans += expand(i, i+1)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.countSubstrings("abc"))  # 3
    print(s.countSubstrings("aaa"))  # 6
