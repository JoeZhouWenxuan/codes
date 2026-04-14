# 148. 排序链表
# https://leetcode.cn/problems/sort-list/
# 难度：中等
#
# 给你链表的头结点 head，请将其按升序排列并返回排序后的链表。
# 要求 O(n log n) 时间复杂度和 O(1) 空间复杂度（迭代归并排序）。
#
# 示例：
# 输入：head = [4,2,1,3]    输出：[1,2,3,4]
# 输入：head = [-1,5,3,4,0] 输出：[-1,0,3,4,5]
#
# 思路：自顶向下递归归并排序（O(log n) 栈空间）
# 若要严格 O(1) 空间可用自底向上迭代版本（见注释）

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     # 递归终止：0或1个节点
    #     if not head or not head.next:
    #         return head

    #     # 快慢指针找中点，将链表从中间断开
    #     slow, fast = head, head.next
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #     mid = slow.next
    #     slow.next = None  # 断开

    #     # 递归排序两段
    #     left = self.sortList(head)
    #     right = self.sortList(mid)

    #     # 合并两段有序链表
    #     return self._merge(left, right)

    # def _merge(self, l1, l2):
    #     dummy = ListNode()
    #     cur = dummy
    #     while l1 and l2:
    #         if l1.val <= l2.val:
    #             cur.next = l1
    #             l1 = l1.next
    #         else:
    #             cur.next = l2
    #             l2 = l2.next
    #         cur = cur.next
    #     cur.next = l1 or l2
    #     return dummy.next

    def sortList(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)
        return self._merge(left, right)

    def _merge(l, r):
        dummy = ListNode()
        curr = dummy
        while l and r:
            if l.val < r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
            curr = curr.next
        curr.next = l or r
        return dummy.next
            
    # def sortList(self, head):
    #     if not head or not head.next:
    #         return head
    #     slow, fast = head, head.next

    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #     mid = slow.next
    #     slow.next = None
    #     left = self.sortList(head)
    #     right = self.sortList(mid)
    #     return self._merge(left, right)
    
    # def _merge(self, l1, l2):
    #     dummy = ListNode()
    #     cur = dummy
    #     while l1 and l2:
    #         if l1.val <= l2.val:
    #             cur.next = l1
    #             l1 = l1.next
    #         else:
    #             cur.next = l2
    #             l2 = l2.next
    #         cur = cur.next
    #     cur.next = l1 or l2
    #     return dummy.next



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
    print_list(s.sortList(make_list([4, 2, 1, 3])))       # [1, 2, 3, 4]
    print_list(s.sortList(make_list([-1, 5, 3, 4, 0])))   # [-1, 0, 3, 4, 5]
