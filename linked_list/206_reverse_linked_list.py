# 206. 反转链表
# https://leetcode.cn/problems/reverse-linked-list/
# 难度：简单
#
# 给你单链表的头节点 head，请你反转链表，并返回反转后的链表。
#
# 示例：
# 输入：head = [1,2,3,4,5]  输出：[5,4,3,2,1]

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     prev, curr = None, head
    #     while curr:
    #         nxt = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = nxt
    #     return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            # nxt = curr.next
            # curr.next = prev
            # prev = curr
            # curr = nxt
            curr.next, prev, curr = prev, curr, curr.next
        return prev


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
    print_list(s.reverseList(make_list([1, 2, 3, 4, 5])))  # [5, 4, 3, 2, 1]
    print_list(s.reverseList(make_list([1, 2])))            # [2, 1]
