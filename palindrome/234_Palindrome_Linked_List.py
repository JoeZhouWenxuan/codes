# 234. 回文链表
# https://leetcode.cn/problems/palindrome-linked-list/
# 难度：简单
#
# 给你一个单链表的头节点 head，请你判断该链表是否为回文链表。
#
# 示例：
# 输入：head = [1,2,2,1]  输出：True
# 输入：head = [1,2]      输出：False

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # slow, fast = head, head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # prev, curr = None, slow
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt

        # left, right = head, prev
        # while right:
        #     if left.val != right.val:
        #         return False
        #     left = left.next
        #     right = right.next

        # return True

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


def make_list(vals):
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(make_list([1, 2, 2, 1])))  # True
    print(s.isPalindrome(make_list([1, 2])))         # False
