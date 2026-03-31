# 207. 课程表
# https://leetcode.cn/problems/course-schedule/
# 难度：中等
#
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1。
# 在选修某些课程之前需要一些先修课程。先修课程按数组 prerequisites 给出，
# 其中 prerequisites[i] = [ai, bi] 表示如果要学习课程 ai 则必须先学习课程 bi。
# 请你判断是否可能完成所有课程的学习。
#
# 示例：
# 输入：numCourses = 2, prerequisites = [[1,0]]      输出：True
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]] 输出：False

from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        visited = 0

        while queue:
            node = queue.popleft()
            visited += 1
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return visited == numCourses


if __name__ == "__main__":
    s = Solution()
    print(s.canFinish(2, [[1, 0]]))            # True
    print(s.canFinish(2, [[1, 0], [0, 1]]))    # False
