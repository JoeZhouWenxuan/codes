# 25. K 个一组翻转链表
# https://leetcode.cn/problems/reverse-nodes-in-k-group/
# 难度：困难
#
# 给你链表的头节点 head，每 k 个节点一组进行翻转，请你返回修改后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 示例：
# 输入：head = [1,2,3,4,5], k = 2  输出：[2,1,4,3,5]
# 输入：head = [1,2,3,4,5], k = 3  输出：[3,2,1,4,5]

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 检查剩余节点是否足够 k 个
        cur = head
        for _ in range(k):
            if not cur:
                return head  # 不足 k 个，原样返回
            cur = cur.next

        # 反转前 k 个节点
        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # head 现在是翻转后的尾节点，连接后续递归结果
        head.next = self.reverseKGroup(curr, k)
        return prev  # prev 是翻转后的头节点


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
    print_list(s.reverseKGroup(make_list([1, 2, 3, 4, 5]), 2))  # [2, 1, 4, 3, 5]
    print_list(s.reverseKGroup(make_list([1, 2, 3, 4, 5]), 3))  # [3, 2, 1, 4, 5]
