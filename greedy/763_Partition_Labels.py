# 763. 划分字母区间
# https://leetcode.cn/problems/partition-labels/
# 难度：中等
#
# 给你一个字符串 s。把这个字符串划分为尽可能多的片段，
# 同一字母最多出现在一个片段中。返回每个片段的长度。
#
# 示例：
# 输入：s = "ababcbacadefegdehijhklij"  输出：[9,7,8]
# 输入：s = "eccbbbbdec"                 输出：[10]

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # last[ch] 表示字符 ch 最后一次出现的位置。
        last = {ch: i for i, ch in enumerate(s)}

        ans = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            # 当前片段必须至少覆盖到 ch 的最后出现位置。
            end = max(end, last[ch])

            # i 到达 end，说明当前片段里的所有字符都不会出现在后面，可以切分。
            if i == end:
                ans.append(end - start + 1)
                start = i + 1

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij"))  # [9, 7, 8]
    print(s.partitionLabels("eccbbbbdec"))                 # [10]

