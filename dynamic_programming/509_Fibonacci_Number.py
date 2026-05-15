# 509. 斐波那契数
# https://leetcode.cn/problems/fibonacci-number/
# 难度：简单
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2)
#
# 示例：
# 输入：n = 2    输出：1
# 输入：n = 4    输出：3
#
# 和爬楼梯关系：
# 爬楼梯是 dp[1] = 1, dp[2] = 2；
# 斐波那契是 fib[0] = 0, fib[1] = 1。
# 两者都是“当前状态依赖前两个状态”的线性 DP。


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        prev, curr = 0, 1
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr

        return curr


if __name__ == "__main__":
    s = Solution()
    print(s.fib(2))  # 1
    print(s.fib(4))  # 3

