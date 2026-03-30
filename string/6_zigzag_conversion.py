# 6. Z 字形变换
# https://leetcode.cn/problems/zigzag-conversion/
# 难度：中等
#
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串。
#
# 示例：
# 输入：s = "PAYPALISHIRING", numRows = 3    输出："PAHNAPLSIIGYIR"
# 输入：s = "PAYPALISHIRING", numRows = 4    输出："PINALSIGYAHRPI"


class Solution:
    # def convert(self, s: str, numRows: int) -> str:
    #     if numRows == 1 or numRows >= len(s):
    #         return s

    #     rows = [""] * numRows
    #     row = 0
    #     step = 1

    #     for ch in s:
    #         rows[row] += ch
    #         if row == 0:
    #             step = 1
    #         elif row == numRows - 1:
    #             step = -1
    #         row += step

    #     return "".join(rows)
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        curr_row = 0
        step = 1
        for i, ch in enumerate(s):
            rows[curr_row] += ch
            if curr_row == 0:
                step = 1
            elif curr_row == numRows - 1:
                step = -1
            curr_row += step
        return "".join(rows)

        

if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
    print(s.convert("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
