# 39. 组合总和
# https://leetcode.cn/problems/combination-sum/
# 难度：中等
#
# 给你一个无重复元素的整数数组 candidates 和一个目标整数 target，
# 找出 candidates 中可以使数字和为目标数 target 的所有不同组合，
# 每个数字可以无限制重复选取。答案中的组合不能重复，可以按任意顺序返回。
#
# 示例：
# candidates = [2,3,6,7], target = 7 → [[2,2,3],[7]]
# candidates = [2,3,5],   target = 8 → [[2,2,2,2],[2,3,3],[3,5]]
#
# ┌──────────────────────────────────────────────────────────────┐
# │ 解法对比                                                      │
# │  1. 回溯 + 剪枝    O(n^(t/m)) 时间  O(t/m) 空间  推荐        │
# │  2. 回溯（无剪枝）  同上但常数更大    同上        仅作对比     │
# │  n=候选数量, t=target, m=最小候选值                           │
# └──────────────────────────────────────────────────────────────┘

from typing import List


# ── 解法一：回溯 + 排序剪枝 ───────────────────────────────────
# 从 start 位置向后枚举，避免产生重复组合（如 [2,3] 和 [3,2]）。
# 排序后当 candidates[i] > remaining 时直接 break，剪去后续所有分支。
# 时间 O(n^(t/m))，空间 O(t/m) 递归栈深度
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start: int, path: List[int], remaining: int):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:   # 剪枝：后续更大，直接终止
                    break
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])  # i 不+1，可重复选
                path.pop()

        backtrack(0, [], target)
        return res


# ── 解法二：回溯（无剪枝，对比用） ────────────────────────────
# 不排序、不 break，靠 remaining < 0 的条件终止。
# 逻辑更直白，但会多走很多无效分支。
class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start: int, path: List[int], remaining: int):
            if remaining == 0:
                res.append(path[:])
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return res


if __name__ == "__main__":
    cases = [
        ([2, 3, 6, 7], 7,  [[2, 2, 3], [7]]),
        ([2, 3, 5],    8,  [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([1],          1,  [[1]]),
    ]

    for Cls in [Solution, Solution2]:
        print(Cls.__name__)
        for candidates, target, expected in cases:
            result = sorted(sorted(r) for r in Cls().combinationSum(candidates[:], target))
            exp    = sorted(sorted(r) for r in expected)
            status = "OK" if result == exp else f"FAIL (got {result})"
            print(f"  {candidates}, {target} → {result}  {status}")
