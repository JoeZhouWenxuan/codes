# 94. 二叉树的中序遍历
# https://leetcode.cn/problems/binary-tree-inorder-traversal/
# 难度：简单
#
# 给定一个二叉树的根节点 root ，返回它的中序遍历。
#
# 示例：
# 输入：root = [1,null,2,3]  输出：[1,3,2]
# 输入：root = []            输出：[]

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res

    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            res.append(current.val)
            current = current.right

        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res

    def preorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res

    def postorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res[::-1]

    def postorderTraversalIterativePrev(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        prev = None
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            node = stack[-1]
            if node.right and prev != node.right:
                current = node.right
            else:
                res.append(node.val)
                prev = stack.pop()

        return res

    def postorderTraversalIterativeTwoStacks(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack1 = [root]
        stack2 = []
        res = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            res.append(stack2.pop().val)

        return res

    def postorderTraversalIterativeMarked(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                res.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return res


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


if __name__ == "__main__":
    s = Solution()
    root = build_tree([1, None, 2, 3])

    print(s.inorderTraversal(root))           # [1, 3, 2]
    print(s.inorderTraversalIterative(root))  # [1, 3, 2]

    print(s.preorderTraversal(root))           # [1, 2, 3]
    print(s.preorderTraversalIterative(root))  # [1, 2, 3]

    print(s.postorderTraversal(root))           # [3, 2, 1]
    print(s.postorderTraversalIterative(root))  # [3, 2, 1]
    print(s.postorderTraversalIterativePrev(root))       # [3, 2, 1]
    print(s.postorderTraversalIterativeTwoStacks(root))  # [3, 2, 1]
    print(s.postorderTraversalIterativeMarked(root))     # [3, 2, 1]

    empty = build_tree([])
    print(s.inorderTraversal(empty))            # []
    print(s.preorderTraversal(empty))           # []
    print(s.postorderTraversal(empty))          # []
