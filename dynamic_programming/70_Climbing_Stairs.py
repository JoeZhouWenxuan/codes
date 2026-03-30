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


class Solution:
    def climbStairs(self, n: int) -> int:
        # if n <= 2:
        #     return n

        # first, second = 1, 2
        # for _ in range(3, n + 1):
        #     first, second = second, first + second

        # return second
        if n <= 2:
            return n
        
        a, b = 1, 2
        for _ in range(3, n+1):
            a, b = b, a+b
        return b

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(2))  # 2
    print(s.climbStairs(3))  # 3
