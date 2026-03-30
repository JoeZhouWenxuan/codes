# 76. 最小覆盖子串
# https://leetcode.cn/problems/minimum-window-substring/
# 难度：困难
#
# 给你一个字符串 s、一个字符串 t。返回 s 中涵盖 t 所有字符的最小子串。
# 如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 ""。
#
# 示例：
# 输入：s = "ADOBECODEBANC", t = "ABC"  输出："BANC"
# 输入：s = "a", t = "a"               输出："a"
# 输入：s = "a", t = "aa"              输出：""
#
# 思路：滑动窗口，用 need 记录还缺少的字符数量，remain 记录还缺少的字符种数。
# 右指针扩张满足条件后，左指针收缩寻找最小窗口。

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # need = Counter(t)    # 还需要的各字符数量
        # remain = len(need)   # 还未满足的字符种数

        # left = 0
        # ans_start, ans_len = 0, float('inf')

        # for right, ch in enumerate(s):
        #     if ch in need:
        #         need[ch] -= 1
        #         if need[ch] == 0:
        #             remain -= 1  # 该字符已满足

        #     # 窗口已覆盖 t，尝试收缩左边界
        #     while remain == 0:
        #         if right - left + 1 < ans_len:
        #             ans_start = left
        #             ans_len = right - left + 1

        #         left_ch = s[left]
        #         left += 1
        #         if left_ch in need:
        #             need[left_ch] += 1
        #             if need[left_ch] > 0:
        #                 remain += 1  # 收缩后该字符不够了

        # return "" if ans_len == float('inf') else s[ans_start:ans_start + ans_len]

        counts = Counter(t)
        remain = len(counts)
        left = 0
        ans_start, ans_len = 0, float('inf')
        '''
            右指针右移，是不是待匹配元素，
                是待匹配元素: counts对应元素个数-1， 如果对应元素个数为0，remain应-1

            while remain == 0 # 满足结果的状态下
                1. 更新结果
                2. 取左侧元素（待左指针右移）
                3. 更新counts对应元素个数+1（待匹配的元素个数+1）
                4. remain需要counts的元素状态需不需要+1（大于0）
                4. 左指针右移
        '''
        for right, x in enumerate(s):
            if x in counts:
                counts[x] -= 1
                if counts[x] == 0:
                    remain -= 1
            
            while remain == 0:
                if right - left + 1 < ans_len:
                    ans_start = left
                    ans_len = right - left + 1
                left_char = s[left]
                left += 1
                if left_char in counts:
                    counts[left_char] += 1
                if counts[left_char] > 0:
                    remain += 1

        return s[ans_start, ans_start + ans_len] if ans_len != float('inf') else ""

if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
    print(s.minWindow("a", "a"))                # "a"
    print(s.minWindow("a", "aa"))               # ""
