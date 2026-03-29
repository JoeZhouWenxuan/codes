# 297. 二叉树的序列化与反序列化
# https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/
# 难度：困难
#
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
# 同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
# 设计一个算法来实现二叉树的序列化与反序列化。
#
# 示例：
# 输入：root = [1,2,3,null,null,4,5]
# 输出：serialize(root) = "1,2,#,#,3,4,#,#,5,#,#"

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        vals = []

        def dfs(node):
            if not node:
                vals.append("#")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(vals)

    def deserialize(self, data):
        vals = deque(data.split(","))

        def dfs():
            if vals[0] == "#":
                vals.popleft()
                return None
            node = TreeNode(int(vals.popleft()))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


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
    codec = Codec()
    root = build_tree([1, 2, 3, None, None, 4, 5])
    data = codec.serialize(root)
    print(data)
    print(codec.serialize(codec.deserialize(data)))
