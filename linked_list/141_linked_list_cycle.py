# 141. 环形链表
# https://leetcode.cn/problems/linked-list-cycle/
# 难度：简单
#
# 给你一个链表的头节点 head，判断链表中是否有环。
# 如果链表中存在环，则返回 true；否则，返回 false。
#
# 示例：
# 输入：head = [3,2,0,-4], pos = 1（尾节点连接到索引1）  输出：true
# 输入：head = [1,2], pos = 0                            输出：true
# 输入：head = [1], pos = -1                             输出：false

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 快慢指针：快指针每次走2步，慢指针每次走1步
        # 若有环，快慢指针必然相遇
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


if __name__ == "__main__":
    s = Solution()

    # 构造有环链表：3 -> 2 -> 0 -> -4 -> (回到2)
    n1, n2, n3, n4 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n2
    print(s.hasCycle(n1))  # True

    # 无环链表
    a, b = ListNode(1), ListNode(2)
    a.next = b
    print(s.hasCycle(a))   # False
