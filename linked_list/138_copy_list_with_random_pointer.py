# 138. 随机链表的复制
# https://leetcode.cn/problems/copy-list-with-random-pointer/
# 难度：中等
#
# 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random，
# 该指针可以指向链表中的任何节点或空节点。
# 构造这个链表的深拷贝，返回复制链表的头节点。
#
# 思路：哈希表存储原节点到新节点的映射，两次遍历完成深拷贝。

from typing import Optional


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        # 原节点 -> 新节点 的映射
        node_map = {}

        # 第一遍：创建所有新节点
        cur = head
        while cur:
            node_map[cur] = Node(cur.val)
            cur = cur.next

        # 第二遍：设置 next 和 random 指针
        cur = head
        while cur:
            if cur.next:
                node_map[cur].next = node_map[cur.next]
            if cur.random:
                node_map[cur].random = node_map[cur.random]
            cur = cur.next

        return node_map[head]


if __name__ == "__main__":
    s = Solution()

    # 构造：[[7,null],[13,0],[11,4],[10,2],[1,0]]
    nodes = [Node(7), Node(13), Node(11), Node(10), Node(1)]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    nodes[2].next = nodes[3]
    nodes[3].next = nodes[4]
    nodes[1].random = nodes[0]
    nodes[2].random = nodes[4]
    nodes[3].random = nodes[2]
    nodes[4].random = nodes[0]

    new_head = s.copyRandomList(nodes[0])
    cur = new_head
    while cur:
        r = cur.random.val if cur.random else None
        print(f"val={cur.val}, random={r}")
        cur = cur.next
