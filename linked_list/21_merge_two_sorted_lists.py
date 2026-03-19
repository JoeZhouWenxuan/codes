# 21. 合并两个有序链表
# https://leetcode.cn/problems/merge-two-sorted-lists/
# 难度：简单
#
# 将两个升序链表合并为一个新的升序链表并返回。
# 新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
# 输入：l1 = [1,2,4], l2 = [1,3,4]  输出：[1,1,2,3,4,4]

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
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
    print_list(s.mergeTwoLists(make_list([1, 2, 4]), make_list([1, 3, 4])))  # [1, 1, 2, 3, 4, 4]
    print_list(s.mergeTwoLists(make_list([]), make_list([])))                # []
