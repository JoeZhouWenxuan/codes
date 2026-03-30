# 406. 根据身高重建队列
# https://leetcode.cn/problems/queue-reconstruction-by-height/
# 难度：中等
#
# 假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性，
# 其中 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面正好有 ki 个身高大于或等于 hi 的人。
# 请你重新构造并返回输入数组 people 所表示的队列。
#
# 示例：
# 输入：people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# 输出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        queue = []

        for person in people:
            queue.insert(person[1], person)

        return queue


if __name__ == "__main__":
    s = Solution()
    print(
        s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
    )  # [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
