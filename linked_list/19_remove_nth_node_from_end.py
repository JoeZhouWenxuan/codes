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
        # dummy 指向头节点前面，方便统一处理“删除头节点”的情况。
        dummy = ListNode(0, head)
        fast = slow = dummy

        # fast 先走 n 步，让 fast 和 slow 之间相隔 n 个节点。
        for _ in range(n):
            fast = fast.next

        # 当 fast 到达最后一个节点时，slow 正好停在待删除节点的前一个节点。
        while fast.next:
            fast = fast.next
            slow = slow.next

        # 删除 slow 后面的节点，也就是倒数第 n 个节点。
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
        # fast 先走 n 步，让 slow 和 fast 保持 n 个节点的距离。
        for _ in range(n):
            fast = fast.next
        # fast 到达尾节点时，slow 位于待删节点的前驱。
        while fast.next:
            fast = fast.next
            slow = slow.next

        # 跳过待删节点。
        slow.next = slow.next.next

        return dummy.next
    
        dummy = ListNode(0, head)
        slow = fast = dummy
        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

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
