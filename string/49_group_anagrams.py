# 49. 字母异位词分组
# https://leetcode.cn/problems/group-anagrams/
# 难度：中等
#
# 给你一个字符串数组，请你将字母异位词组合在一起。
# 字母异位词是由重新排列源单词的所有字母得到的一个新单词。
#
# 示例：
# 输入：strs = ["eat","tea","tan","ate","nat","bat"]
# 输出：[["bat"],["nat","tan"],["ate","eat","tea"]]
#
# 思路：以排序后的字符串作为哈希表的 key，将同组异位词归类。

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))  # 排序后相同的词是异位词
            groups[key].append(word)
        return list(groups.values())


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(s.groupAnagrams([""]))    # [['']]
    print(s.groupAnagrams(["a"]))   # [['a']]
