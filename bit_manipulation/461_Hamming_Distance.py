# 461. 汉明距离
# https://leetcode.cn/problems/hamming-distance/
# 难度：简单
#
# 两个整数之间的汉明距离，指的是这两个数字对应二进制位不同的位置的数目。
# 给你两个整数 x 和 y，计算并返回它们之间的汉明距离。
#
# 示例：
# 输入：x = 1, y = 4    输出：2
# 输入：x = 3, y = 1    输出：1


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # diff = x ^ y
        # count = 0

        # while diff:
        #     diff &= diff - 1
        #     count += 1

        # return count
        diff = x ^ y
        count = 0
        while diff:
            diff &= diff - 1
            count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.hammingDistance(1, 4))  # 2
    print(s.hammingDistance(3, 1))  # 1
