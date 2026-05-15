# 70. 爬楼梯
# https://leetcode.cn/problems/climbing-stairs/
# 难度：简单
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 示例：
# 输入：n = 2    输出：2
# 输入：n = 3    输出：3
#
# 相关题目：
# - 509. 斐波那契数：最基础的前两项递推
# - 746. 使用最小花费爬楼梯：从“方案数”变成“最小代价”
# - 1137. 第 N 个泰波那契数：从依赖前 2 项变成依赖前 3 项
# - 377. 组合总和 IV：从固定步长 1/2，扩展成任意 nums 中的步长


class Solution:
    def climbStairs(self, n: int) -> int:
        # if n <= 2:
        #     return n

        # first, second = 1, 2
        # for _ in range(3, n + 1):
        #     first, second = second, first + second

        # return second
        # dp[i] 表示爬到第 i 阶的方法数。
        # 到达第 i 阶，最后一步只能从 i - 1 爬 1 阶，或从 i - 2 爬 2 阶。
        # 所以 dp[i] = dp[i - 1] + dp[i - 2]。
        if n <= 2:
            return n
        # a 表示 dp[i - 2]，b 表示 dp[i - 1]。
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a+b
        return b

    def climbStairsDP(self, n: int) -> int:
        # 普通 DP 数组写法，方便看清状态定义。
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(2))  # 2
    print(s.climbStairs(3))  # 3
    print(s.climbStairsDP(2))  # 2
    print(s.climbStairsDP(3))  # 3
