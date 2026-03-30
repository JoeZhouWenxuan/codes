# 49. 字母异位词分组
# https://leetcode.cn/problems/group-anagrams/
# 难度：中等
#
# 给你一个字符串数组，请你将字母异位词组合在一起。
#
# 示例：
# 输入：strs = ["eat","tea","tan","ate","nat","bat"]
# 输出：[["bat"],["nat","tan"],["ate","eat","tea"]]

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            groups[key].append(word)

        return list(groups.values())
    
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        # groups = defaultdict(list)

        # for word in strs:
        #     count = [0] * 26
        #     for char in word:
        #         count[ord(char) - ord("a")] += 1
        #     key = tuple(count)
        #     groups[key].append(word)

        # return list(groups.values())
        # groups = defaultdict(list)
        # for word in strs:
        #     count = [0] * 26
        #     for x in word:
        #         count[ord[x] - ord['a']] += 1
        #     key = tuple(count)
        #     groups[key].append(word)
        # return list(groups.values())

        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord[ch] - ord['a']] += 1
            key = tuple(count)
            groups[key].append(word)
        
        return list(groups.values())



if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(s.groupAnagrams([""]))
