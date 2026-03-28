# 17. 电话号码的字母组合
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
# 难度：中等
#
# 给定一个仅包含数字 2-9 的字符串 digits，返回所有它能表示的字母组合。
#
# 示例：
# 输入：digits = "23"    输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 输入：digits = ""      输出：[]

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = []
        path = []

        def backtrack(index: int) -> None:
            if index == len(digits):
                ans.append("".join(path))
                return

            for ch in mapping[digits[index]]:
                path.append(ch)
                backtrack(index + 1)
                path.pop()

        backtrack(0)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))
    print(s.letterCombinations(""))
