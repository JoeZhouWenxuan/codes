# 114. 二叉树展开为链表
# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
# 难度：中等
#
# 给你二叉树的根结点 root ，请你将它展开为一个单链表：
#   1. 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点
#   2. left 子指针始终为 null
#   3. 展开后的单链表应该与二叉树前序遍历顺序相同
#
# 示例：
# 输入：root = [1,2,5,3,4,null,6]
# 输出：1 -> 2 -> 3 -> 4 -> 5 -> 6

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # 解法一：递归返回“展开后链表的尾节点”
        # 先分别展开左右子树，再把左链表插到 node 和右链表之间。
        # dfs(node) 返回以 node 为根的整条右链表的尾节点，方便父节点继续拼接。
        # def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
        #     if not node:
        #         return None

        #     left_tail = dfs(node.left)
        #     right_tail = dfs(node.right)

        #     if left_tail:
        #         left_tail.right = node.right
        #         node.right = node.left
        #         node.left = None

        #     return right_tail or left_tail or node

        # dfs(root)


        def dfs(node):
            if not node:
                return None
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            return right_tail or left_tail or node
        dfs(root)

    # def flatten(self, root):
    #     if not root:
    #         return

    #     self.flatten(root.left)
    #     self.flatten(root.right)

    #     left = root.left
    #     right = root.right

    #     root.left = None
    #     root.right = left

    #     cur = root
    #     while cur.right:
    #         cur = cur.right
    #     cur.right = right


    # prev = None
    # def flatten(root):
    #     if not root:
    #         return
    #     flatten(root.right)
    #     flatten(root.left)
    #     root.right = prev
    #     root.left = None
    #     prev = root


    def flatten_iterative_stack(self, root: Optional[TreeNode]) -> None:
        # 解法二：栈模拟前序遍历
        # 前序顺序是 根 -> 左 -> 右，因此栈中先压右再压左。
        # 每次把当前节点接到前一个访问节点的 right 上，left 清空。
        if not root:
            return

        stack = [root]
        prev = None

        while stack:
            node = stack.pop()
            if prev:
                prev.left = None
                prev.right = node

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            prev = node

    def flatten_morris(self, root: Optional[TreeNode]) -> None:
        # 解法三：Morris 风格原地展开
        # 如果当前节点有左子树，就找到左子树最右节点，
        # 把原右子树接到它后面，再把左子树整体挪到右边。
        cur = root

        while cur:
            if cur.left:
                predecessor = cur.left
                while predecessor.right:
                    predecessor = predecessor.right

                predecessor.right = cur.right
                cur.right = cur.left
                cur.left = None

            cur = cur.right


def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def right_chain_values(root):
    res = []
    while root:
        res.append(root.val)
        root = root.right
    return res


if __name__ == "__main__":
    s = Solution()

    root1 = build_tree([1, 2, 5, 3, 4, None, 6])
    s.flatten(root1)
    print(right_chain_values(root1))  # [1, 2, 3, 4, 5, 6]

    root2 = build_tree([1, 2, 5, 3, 4, None, 6])
    s.flatten_iterative_stack(root2)
    print(right_chain_values(root2))  # [1, 2, 3, 4, 5, 6]

    root3 = build_tree([1, 2, 5, 3, 4, None, 6])
    s.flatten_morris(root3)
    print(right_chain_values(root3))  # [1, 2, 3, 4, 5, 6]
