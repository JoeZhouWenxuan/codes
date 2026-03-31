# 739. 每日温度
# https://leetcode.cn/problems/daily-temperatures/
# 难度：中等
#
# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，
# 其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。
# 如果气温在这之后都不会升高，请在该位置用 0 来代替。
#
# 示例：
# 输入：temperatures = [73,74,75,71,69,72,76,73]    输出：[1,1,4,2,1,1,0,0]
# 输入：temperatures = [30,40,50,60]                输出：[1,1,1,0]

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ans = [0] * len(temperatures)
        # stack = []

        # for i, temp in enumerate(temperatures):
        #     while stack and temperatures[stack[-1]] < temp:
        #         prev = stack.pop()
        #         ans[prev] = i - prev
        #     stack.append(i)

        # return ans
        ans = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                ans[prev] = i - prev    # 注意这里不是ans[i] = 
            stack.append(i)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1, 1, 4, 2, 1, 1, 0, 0]
    print(s.dailyTemperatures([30, 40, 50, 60]))                  # [1, 1, 1, 0]
