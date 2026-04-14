# 24. 两两交换链表中的节点
# https://leetcode.cn/problems/swap-nodes-in-pairs/
# 难度：中等
#
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
# 你必须在不修改节点内部值的情况下完成本题，只能进行节点交换。
#
# 示例：
# 输入：head = [1,2,3,4]  输出：[2,1,4,3]
# 输入：head = []         输出：[]

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 思路：
        # 1. 用 dummy 统一处理头节点也要参与交换的情况。
        # 2. 每次取出相邻的两个节点 first、second。
        # 3. 调整三条指针：
        #    prev -> second -> first -> next_pair
        # 4. 然后把 prev 移到 first，继续处理下一对节点。
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first

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
    print_list(s.swapPairs(make_list([1, 2, 3, 4])))  # [2, 1, 4, 3]
    print_list(s.swapPairs(make_list([])))            # []
    print_list(s.swapPairs(make_list([1])))           # [1]
