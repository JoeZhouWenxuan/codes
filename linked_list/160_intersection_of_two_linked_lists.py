# 160. 相交链表
# https://leetcode.cn/problems/intersection-of-two-linked-lists/
# 难度：简单
#
# 给你两个单链表的头节点 headA 和 headB，请你找出并返回两个单链表相交的起始节点。
# 如果两个链表不存在相交节点，返回 null。
#
# 核心思路（双指针消除长度差）：
#   指针 A 遍历完 listA 后转到 listB；指针 B 遍历完 listB 后转到 listA。
#   两者走过的总路程相同（a + c + b == b + c + a），若有交点必然同时到达。

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # a, b = headA, headB
        # while a is not b:
        #     a = a.next if a else headB
        #     b = b.next if b else headA
        # return a  # 相交节点 或 None（同时走到末尾）
        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
            


if __name__ == "__main__":
    s = Solution()

    # 构造相交链表：A=[4,1,8,4,5], B=[5,6,1,8,4,5]，交点为节点8
    common = ListNode(8)
    common.next = ListNode(4)
    common.next.next = ListNode(5)

    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = common

    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = common

    print(s.getIntersectionNode(headA, headB).val)  # 8
