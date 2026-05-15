# 1137. 第 N 个泰波那契数
# https://leetcode.cn/problems/n-th-tribonacci-number/
# 难度：简单
#
# T0 = 0, T1 = 1, T2 = 1
# Tn = Tn-1 + Tn-2 + Tn-3
#
# 示例：
# 输入：n = 4     输出：4
# 输入：n = 25    输出：1389537
#
# 和爬楼梯关系：
# 爬楼梯每次可走 1 或 2 阶，所以依赖前 2 项；
# 如果每次可走 1、2、3 阶，方案数就会变成依赖前 3 项的泰波那契模型。


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c


if __name__ == "__main__":
    s = Solution()
    print(s.tribonacci(4))   # 4
    print(s.tribonacci(25))  # 1389537

