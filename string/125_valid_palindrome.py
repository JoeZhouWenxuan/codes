# 125. 验证回文串
# https://leetcode.cn/problems/valid-palindrome/
# 难度：简单
#
# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，
# 短语正着读和反着读都一样。则可以认为该短语是一个回文串。
#
# 示例：
# 输入：s = "A man, a plan, a canal: Panama"    输出：True
# 输入：s = "race a car"                        输出：False


class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [ch.lower() for ch in s if ch.isalnum()]
        left, right = 0, len(filtered) - 1

        while left < right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(s.isPalindrome("race a car"))                      # False
