# 399. 除法求值
# https://leetcode.cn/problems/evaluate-division/
# 难度：中等
#
# 给你一个变量对数组 equations 和一个实数值数组 values。
# equations[i] = [Ai, Bi]，values[i] 表示 Ai / Bi = values[i]。
# 对每个查询 queries[j] = [Cj, Dj]，返回 Cj / Dj 的结果。
# 如果结果不存在，返回 -1.0。
#
# 示例：
# 输入：
# equations = [["a","b"],["b","c"]]
# values = [2.0,3.0]
# queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# 输出：[6.0,0.5,-1.0,1.0,-1.0]
#
# 思路：带权图 + DFS。
# a / b = 2.0 可以看成两条有向边：
# a -> b，权重 2.0
# b -> a，权重 1 / 2.0
# 查询 x / y 时，就是在图中找一条从 x 到 y 的路径，并把路径上的权重相乘。

from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        graph = defaultdict(list)

        # 建立带权图。
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1.0 / value))

        def dfs(start: str, end: str, visited: set[str]) -> float:
            # 题目约定：如果变量不存在，结果为 -1.0。
            if start not in graph or end not in graph:
                return -1.0

            if start == end:
                return 1.0

            visited.add(start)

            for nxt, weight in graph[start]:
                if nxt in visited:
                    continue

                # sub_result 表示 nxt / end 的结果。
                sub_result = dfs(nxt, end, visited)
                if sub_result != -1.0:
                    # start / end = start / nxt * nxt / end
                    return weight * sub_result

            return -1.0

        ans = []
        for a, b in queries:
            ans.append(dfs(a, b, set()))

        return ans


if __name__ == "__main__":
    s = Solution()
    print(
        s.calcEquation(
            [["a", "b"], ["b", "c"]],
            [2.0, 3.0],
            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
        )
    )  # [6.0, 0.5, -1.0, 1.0, -1.0]

