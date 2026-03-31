# LeetCode 图论专题题解

## 一、graph 目录 — 图论专题

本文把 LeetCode 中常见的图论题集中整理，方便按“DFS、BFS、拓扑排序、并查集”来复习。

| 题号 | 题目 | 难度 | 核心标签 |
|------|------|------|----------|
| 207 | 课程表 | 中等 | 拓扑排序、有向图判环 |

---

## 二、第 207 题详解 — 课程表

### 题目描述
给定课程总数 `numCourses` 和先修关系 `prerequisites`，判断是否可以完成所有课程学习。

### 示例
- `numCourses = 2, prerequisites = [[1,0]]` -> `True`
- `numCourses = 2, prerequisites = [[1,0],[0,1]]` -> `False`

### 核心思路：拓扑排序判断图中是否有环

把课程依赖关系看成有向图：
- `bi -> ai` 表示先学 `bi` 才能学 `ai`

如果图中存在环，就不可能完成所有课程。

做法：
- 统计每个节点入度
- 把所有入度为 `0` 的课程入队
- 不断弹出并删除它对后继课程的影响
- 最后如果访问节点数等于课程总数，说明无环

#### 代码
```python
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
```

#### 复杂度
- 时间复杂度：**O(V + E)**
- 空间复杂度：**O(V + E)**
