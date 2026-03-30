# 19. 删除链表的倒数第 N 个节点
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
# 难度：中等
#
# 给你一个链表，删除链表的倒数第 n 个节点，并且返回链表的头节点。
#
# 示例：
# 输入：head = [1,2,3,4,5], n = 2  输出：[1,2,3,5]
# 输入：head = [1], n = 1          输出：[]
#
# 思路：快慢指针，快指针先走 n 步，然后快慢同步前进，
# 快指针到末尾时慢指针正好在倒数第 n+1 个节点（待删节点的前驱）。

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        # 快指针先走 n+1 步
        for _ in range(n + 1):
            fast = fast.next

        # 同步前进直到快指针到末尾
        while fast:
            fast = fast.next
            slow = slow.next

        # slow 此时是待删节点的前驱
        slow.next = slow.next.next
        return dummy.next

    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy = ListNode(0, head)
        # slow = fast = dummy
        # for _ in range(n):
        #     fast = fast.next
        
        # while fast.next:
        #     fast = fast.next
        #     slow = slow.next
        
        # slow.next = slow.next.next

        # return dummy.next
        dummy = ListNode(0, head)
        slow = fast = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

    

def make_list(vals):
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


if __name__ == "__main__":
    s = Solution()
    print_list(s.removeNthFromEnd(make_list([1, 2, 3, 4, 5]), 2))  # [1, 2, 3, 5]
    print_list(s.removeNthFromEnd(make_list([1]), 1))               # []
    print_list(s.removeNthFromEnd(make_list([1, 2]), 1))            # [1]
