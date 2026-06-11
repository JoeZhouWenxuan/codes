# 1352. 最后 K 个数的乘积
# https://leetcode.cn/problems/product-of-the-last-k-numbers/
# 难度：中等
#
# 题目：实现 add(num) 和 getProduct(k)，返回最近 k 个数的乘积。
#
# 思路：
# 维护前缀积数组 products，products[-1] 是当前所有数乘积。
# 遇到 0 时，包含它的乘积都为 0，直接重置前缀积为 [1]。
# 若 k 大于等于当前前缀积长度，说明最近 k 个数里包含 0。


class ProductOfNumbers:
    def __init__(self):
        self.products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.products = [1]
        else:
            self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.products):
            return 0
        return self.products[-1] // self.products[-1 - k]


if __name__ == "__main__":
    obj = ProductOfNumbers()
    for x in [3, 0, 2, 5, 4]:
        obj.add(x)
    print(obj.getProduct(2))  # 20
