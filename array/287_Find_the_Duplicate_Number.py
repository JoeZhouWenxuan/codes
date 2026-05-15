# 287. 寻找重复数
# https://leetcode.cn/problems/find-the-duplicate-number/
# 难度：中等
#
# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 [1, n] 范围内，可知至少存在一个重复的整数。
# 假设 nums 只有一个重复的整数，返回这个重复的数。
#
# 示例：
# 输入：nums = [1,3,4,2,2]    输出：2
# 输入：nums = [3,1,3,4,2]    输出：3

from typing import List


class Solution:
    # def findDuplicate(self, nums: List[int]) -> int:
    #     slow = nums[0]
    #     fast = nums[nums[0]]

    #     while slow != fast:
    #         slow = nums[slow]
    #         fast = nums[nums[fast]]

    #     fast = 0
    #     while slow != fast:
    #         slow = nums[slow]
    #         fast = nums[fast]

    #     return slow

    def findDuplicate(self, nums: List[int]) -> int:
        # 把数组看成链表：下标 i 指向 nums[i]。
        # 因为 nums 中的值都在 [1, n]，所以每次跳转 nums[i] 都会落在合法下标范围内。
        # 如果某个数字重复，说明有多个下标指向同一个位置，链表中一定会形成环。
        # 重复的数字就是这个环的入口。
        slow = nums[0]
        fast = nums[nums[0]]

        # 第一阶段：快慢指针在环内相遇。
        # slow 每次走一步，fast 每次走两步。
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # 第二阶段：从下标 0 和相遇点同时出发，每次都走一步。
        # 两个指针再次相遇的位置就是环入口，也就是重复的数字。
        slow2 = 0 # **注意，这里是0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow

if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate([1, 3, 4, 2, 2]))  # 2
    print(s.findDuplicate([3, 1, 3, 4, 2]))  # 3
