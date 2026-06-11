# LeetCode 图论专题题解

## 一、graph 目录 — 图论专题

本文把 LeetCode 中常见的图论题集中整理，方便按“DFS、BFS、拓扑排序、并查集”来复习。

| 题号 | 题目 | 难度 | 核心标签 |
|------|------|------|----------|
| 207 | 课程表 | 中等 | 拓扑排序、有向图判环 |
| 399 | 除法求值 | 中等 | 带权图、DFS |

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

---

## 三、第 399 题详解 — 除法求值

### 题目描述

给定若干等式：

```python
a / b = value
```

再给定一些查询：

```python
x / y
```

如果可以根据已知等式推导出结果，返回对应值；否则返回 `-1.0`。

### 示例

```python
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
```

输出：

```python
[6.0, 0.5, -1.0, 1.0, -1.0]
```

### 核心思路：带权图

把变量看成图中的节点，把除法关系看成带权边。

如果：

```python
a / b = 2.0
```

则建两条边：

```python
a -> b，权重 2.0
b -> a，权重 0.5
```

查询 `a / c` 时，如果存在路径：

```python
a -> b -> c
```

那么结果就是路径权重乘积：

```python
(a / b) * (b / c)
```

### 代码

```python
from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1.0 / value))

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            visited.add(start)

            for nxt, weight in graph[start]:
                if nxt in visited:
                    continue

                sub_result = dfs(nxt, end, visited)
                if sub_result != -1.0:
                    return weight * sub_result

            return -1.0

        return [dfs(a, b, set()) for a, b in queries]
```

### 复杂度

设变量数为 `V`，等式数为 `E`，查询数为 `Q`：

- 建图时间复杂度：**O(E)**
- 单次查询时间复杂度：**O(V + E)**
- 总时间复杂度：**O(E + Q * (V + E))**
- 空间复杂度：**O(V + E)**
