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
# ┌─────────────────────────────────────────────────────────────┐
# │ 解法对比                                                     │
# │  1. 最小堆      O(n log k) 时间  O(k) 空间   实际最快        │
# │  2. 分治归并    O(n log k) 时间  O(log k) 栈  空间更优       │
# │  3. 顺序合并    O(nk) 时间       O(1) 空间    代码最简        │
# │ 推荐：面试首选分治归并，工程首选最小堆                        │
# └─────────────────────────────────────────────────────────────┘

from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ── 解法一：最小堆 ─────────────────────────────────────────────
# 将 k 个链表的头节点入堆，每次弹出最小节点接到结果链表，
# 再将该节点的下一个节点入堆。堆中始终最多 k 个元素。
# 时间 O(n log k)，空间 O(k)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # (节点值, 链表索引, 节点) — 索引作为第二比较键，避免值相同时比较不可比的 ListNode
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        cur = dummy
        while heap:
            _, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


# ── 解法二：分治归并 ───────────────────────────────────────────
# 类似归并排序：将 k 个链表两两配对合并，每轮链表数减半，
# 共 log k 轮，每轮合并总节点数 n。
# 时间 O(n log k)，空间 O(log k) 递归栈
class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # if not lists:
        #     return None
        # return self._merge_range(lists, 0, len(lists) - 1)

    # def _merge_range(self, lists, l, r):
    #     if l == r:
    #         return lists[l]
    #     mid = (l+r) // 2
    #     left = self._merge_range(lists, l, mid)
    #     right = self._merge_range(lists, mid+1, r)
    #     return self._merge_two(left, right)
    
    # def _merge_two(self, l1, l2):
    #     dummy = ListNode()
    #     cur = dummy
    #     while l1 and l2:
    #         if l1.val <= l2.val:
    #             cur.next, l1 = l1, l1.next
    #         else:
    #             cur.next, l2 = l2, l2.next
    #         cur = cur.next
    #     cur.next = l1 or l2
    #     return dummy.next
        if not lists:
            return None
        return self._merge_range(list, 0, len(lists) - 1)
        
    def _merge_range(self, lists, l, r):
        if l == r:
            return list[l]
        mid = (l + r) // 2
        left = self._merge_range(lists, l, mid)
        right = self._merge_range(lists, mid+1, r)
        return self._merge_two(left, right)
    
    def _merge_two(self, left, right):
        dummy = ListNode()
        curr = dummy
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left or right
        return dummy.next


# ── 解法三：顺序合并 ───────────────────────────────────────────
# 依次将每个链表与结果合并，相当于 k-1 次两路归并。
# k 较大时前几轮结果链表已经很长，效率低。
# 时间 O(nk)，空间 O(1)
class Solution3:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = None
        for node in lists:
            result = self._merge_two(result, node)
        return result

    def _merge_two(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 or l2
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
    for Cls in [Solution, Solution2, Solution3]:
        s = Cls()
        lists = [make_list([1, 4, 5]), make_list([1, 3, 4]), make_list([2, 6])]
        print_list(s.mergeKLists(lists))  # [1, 1, 2, 3, 4, 4, 5, 6]
        print_list(s.mergeKLists([]))     # []
