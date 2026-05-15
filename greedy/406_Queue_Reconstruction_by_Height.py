# 406. 根据身高重建队列
# https://leetcode.cn/problems/queue-reconstruction-by-height/
# 难度：中等
#
# 假设有打乱顺序的一群人，每个人表示为 [h, k]：
# h 是身高，k 是排在这个人前面且身高大于或等于 h 的人数。
# 请重建队列。
#
# 示例：
# 输入：people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# 输出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 先按身高从高到低排序；身高相同则 k 小的在前。
        # 这样插入矮个子时，不会影响已经放好的高个子的 k。
        people.sort(key=lambda x: (-x[0], x[1]))

        ans = []
        for person in people:
            # 当前队列里的人都不矮于 person。
            # 因此把 person 插入下标 k，正好保证前面有 k 个身高 >= h 的人。
            ans.insert(person[1], person)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))

