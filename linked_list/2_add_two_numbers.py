# 2. 两数相加
# https://leetcode.cn/problems/add-two-numbers/
# 难度：中等
#
# 给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序方式存储的，
# 并且每个节点只能存储一位数字。请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 示例：
# 输入：l1 = [2,4,3], l2 = [5,6,4]  输出：[7,0,8]  （342 + 465 = 807）
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]  输出：[8,9,9,9,0,0,0,1]

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0  # 进位

        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, digit = divmod(val, 10)
            cur.next = ListNode(digit)
            cur = cur.next

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
    print_list(s.addTwoNumbers(make_list([2, 4, 3]), make_list([5, 6, 4])))            # [7, 0, 8]
    print_list(s.addTwoNumbers(make_list([9,9,9,9,9,9,9]), make_list([9,9,9,9])))     # [8,9,9,9,0,0,0,1]
