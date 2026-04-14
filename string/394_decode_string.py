# 394. 字符串解码
# https://leetcode.cn/problems/decode-string/
# 难度：中等
#
# 给定一个经过编码的字符串，返回它解码后的字符串。
# 编码规则：k[encoded_string]，表示 encoded_string 重复 k 次。
#
# 示例：
# 输入：s = "3[a]2[bc]"      输出："aaabcbc"
# 输入：s = "3[a2[c]]"       输出："accaccacc"
# 输入：s = "2[abc]3[cd]ef"  输出："abcabccdcdcdef"
#
# 思路：栈。遇到数字累积倍数，遇到 '[' 将当前字符串和倍数压栈，
# 遇到 ']' 弹栈拼接，遇到字母直接追加。

class Solution:
    def decodeString(self, s: str) -> str:
        # stack = []   # 存储 (已构建的字符串, 重复次数)
        # cur_str = ""
        # cur_num = 0

        # for ch in s:
        #     if ch.isdigit():
        #         cur_num = cur_num * 10 + int(ch)
        #     elif ch == '[':
        #         stack.append((cur_str, cur_num))
        #         cur_str, cur_num = "", 0
        #     elif ch == ']':
        #         prev_str, num = stack.pop()
        #         cur_str = prev_str + cur_str * num
        #     else:
        #         cur_str += ch

        # return cur_str

        stack = []
        curr_num = 0
        curr_str = ""
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == '[':
                stack.append((curr_num, curr_str))
                curr_num = 0
                curr_str = ""
            elif ch == ']':
                curr_num, prev_str = stack.pop()
                curr_str = prev_str + curr_num * curr_str
            else:
                curr_str += ch

        return curr_str
            


if __name__ == "__main__":
    s = Solution()
    print(s.decodeString("3[a]2[bc]"))      # "aaabcbc"
    print(s.decodeString("3[a2[c]]"))       # "accaccacc"
    print(s.decodeString("2[abc]3[cd]ef"))  # "abcabccdcdcdef"
    print(s.decodeString("100[a]"))         # "aaa...a"（100个a）
