# 23. 合并 K 个升序链表
# https://leetcode.cn/problems/merge-k-sorted-lists/
# 难度：困难
#
# 给你一个链表数组，每个链表都已经按升序排列。
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
# 示例：
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]  输出：[1,1,2,3,4,4,5,6]
#
# 思路：分治归并，两两合并，时间复杂度 O(n log k)，k 为链表数量。

from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 最小堆：(节点值, 索引, 节点) — 索引保证值相同时比较不会出错
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        cur = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

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
    lists = [make_list([1, 4, 5]), make_list([1, 3, 4]), make_list([2, 6])]
    print_list(s.mergeKLists(lists))  # [1, 1, 2, 3, 4, 4, 5, 6]

    print_list(s.mergeKLists([]))     # []
