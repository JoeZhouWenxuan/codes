# 142. 环形链表 II
# https://leetcode.cn/problems/linked-list-cycle-ii/
# 难度：中等
#
# 给定一个链表的头节点 head，返回链表开始入环的第一个节点。
# 如果链表无环，则返回 null。
#
# 核心数学推导：
#   设链表头到环入口距离为 a，环入口到相遇点距离为 b，环长为 c。
#   快慢指针相遇时：fast 走了 a + b + k*c，slow 走了 a + b。
#   因为 fast = 2 * slow，所以 a + b + k*c = 2*(a+b)，即 a = k*c - b。
#   此时让一个指针从 head 出发，另一个从相遇点出发，每次各走1步，
#   再次相遇点就是环入口。

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow, fast = head, head

        # # 第一阶段：找到快慢指针相遇点
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow is fast:
        #         break
        # else:
        #     return None  # 无环

        # # 第二阶段：一个指针从 head，一个从相遇点，同速前进，再次相遇即入口
        # ptr = head
        # while ptr is not slow:
        #     ptr = ptr.next
        #     slow = slow.next
        # return ptr
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
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
