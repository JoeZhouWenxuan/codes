# 142. 环形链表 II
# https://leetcode.cn/problems/linked-list-cycle-ii/
# 难度：中等
#
# 给定一个链表的头节点 head，返回链表开始入环的第一个节点。
# 如果链表无环，则返回 null。
#
# 核心数学推导：
#   设：
#   - 头节点到环入口的距离为 a
#   - 环入口到第一次相遇点的距离为 b
#   - 环的长度为 c
#
#   当 slow 和 fast 第一次相遇时：
#   - slow 一共走了 a + b
#   - fast 一共走了 a + b + k*c（k >= 1，表示 fast 在环里多转了 k 圈）
#
#   又因为 fast 的速度是 slow 的 2 倍，所以：
#   a + b + k*c = 2 * (a + b)
#
#   化简得：
#   a = k*c - b
#
#   这说明：
#   - 从 head 走到环入口，需要走 a 步
#   - 从相遇点继续往前走到环入口，需要先走 c - b 步回到入口，
#     再走 (k - 1) * c 步绕整圈，合起来也是 k*c - b = a 步
#
#   所以让一个指针从 head 出发，另一个指针从相遇点出发，
#   两者每次都走 1 步，它们会在环入口再次相遇。

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        # 第一阶段：若有环，快慢指针一定会在环内某处相遇
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return None

        # 第二阶段：根据上面的推导，
        # 从 head 出发的指针和从相遇点出发的指针，
        # 同速前进后会在环入口相遇
        ptr = head
        while ptr is not slow:
            ptr = ptr.next
            slow = slow.next

        return ptr


if __name__ == "__main__":
    s = Solution()

    # 有环：3 -> 2 -> 0 -> -4 -> (回到2)，入口为节点2
    n1, n2, n3, n4 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n2
    print(s.detectCycle(n1).val)  # 2

    # 无环
    a = ListNode(1)
    print(s.detectCycle(a))       # None
