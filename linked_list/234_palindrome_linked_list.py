# 234. 回文链表
# https://leetcode.cn/problems/palindrome-linked-list/
# 难度：简单
#
# 给你一个单链表的头节点 head，请你判断该链表是否为回文链表。
# 要求 O(n) 时间复杂度和 O(1) 空间复杂度。
#
# 示例：
# 输入：head = [1,2,2,1]  输出：true
# 输入：head = [1,2]      输出：false
#
# 思路：
# 1. 快慢指针找到链表中点
# 2. 反转后半段链表
# 3. 双指针从两端比较
# 4. 恢复链表（可选）

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 找中点（slow 最终停在前半段末尾）
        # slow, fast = head, head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # # 反转后半段
        # prev, curr = None, slow
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt

        # # 比较前半段和反转后的后半段
        # left, right = head, prev
        # while right:
        #     if left.val != right.val:
        #         return False
        #     left = left.next
        #     right = right.next

        # return True
        # 找中点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 反转后半段
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
    print(s.isPalindrome(make_list([1, 2, 1])))      # True
