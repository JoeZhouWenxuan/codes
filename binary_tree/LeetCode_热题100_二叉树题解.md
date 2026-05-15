# LeetCode 热题 100 二叉树专题整理

## 一、binary_tree 目录 — 二叉树专题

本文按仓库内其他专题文档的格式，整理 LeetCode 热题 100 中常见的二叉树题目。

| 题号 | 题目 | 难度 | 核心标签 |
|------|------|------|----------|
| 94 | 二叉树的中序遍历 | 简单 | DFS、递归、栈 |
| 96 | 不同的二叉搜索树 | 中等 | BST、动态规划 |
| 98 | 验证二叉搜索树 | 中等 | BST、区间递归 |
| 101 | 对称二叉树 | 简单 | 递归、镜像 |
| 102 | 二叉树的层序遍历 | 中等 | BFS、队列 |
| 104 | 二叉树的最大深度 | 简单 | DFS、递归 |
| 105 | 从前序与中序遍历序列构造二叉树 | 中等 | 递归构造、哈希表 |
| 108 | 将有序数组转换为二叉搜索树 | 简单 | 分治、平衡 BST |
| 110 | 平衡二叉树 | 简单 | 树高、剪枝 |
| 114 | 二叉树展开为链表 | 中等 | 指针调整、前序 |
| 124 | 二叉树中的最大路径和 | 困难 | 树形 DP |
| 199 | 二叉树的右视图 | 中等 | BFS、层序遍历 |
| 226 | 翻转二叉树 | 简单 | 递归、交换指针 |
| 230 | 二叉搜索树中第 K 小的元素 | 中等 | BST、中序遍历 |
| 235 | 二叉搜索树的最近公共祖先 | 中等 | BST、区间判断 |
| 236 | 二叉树的最近公共祖先 | 中等 | 递归、分治 |
| 297 | 二叉树的序列化与反序列化 | 困难 | 先序遍历、构造 |
| 337 | 打家劫舍 III | 中等 | 树形 DP |
| 437 | 路径总和 III | 中等 | 前缀和、DFS |
| 538 | 把二叉搜索树转换为累加树 | 中等 | BST、反向中序 |
| 543 | 二叉树的直径 | 简单 | 树形 DP、深度 |
| 617 | 合并二叉树 | 简单 | 递归、节点合并 |

---

## 二、第 94 题详解 — 二叉树的中序遍历

### 题目描述
给定一棵二叉树的根节点 `root`，返回它的中序遍历结果。

### 示例
- `root = [1,null,2,3]` -> `[1,3,2]`
- `root = []` -> `[]`

### 核心思路：递归模拟中序顺序

中序遍历顺序固定为：
- 先遍历左子树
- 再访问当前节点
- 最后遍历右子树

递归写法最直观，也最适合作为后续二叉树题目的基础模板。

#### 代码
```python
class Solution:
    def inorderTraversal(self, root):
        ans = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root)
        return ans
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(h)**，`h` 为树高

---

## 三、第 98 题详解 — 验证二叉搜索树

### 题目描述
给你一个二叉树的根节点 `root`，判断其是否是合法的二叉搜索树。

### 示例
- `root = [2,1,3]` -> `true`
- `root = [5,1,4,null,null,3,6]` -> `false`

### 核心思路：递归维护上下界

对于任意节点，它不仅要和父节点比较，还要满足整条路径传递下来的范围约束。

#### 步骤
1. 根节点初始合法区间为 `(-inf, +inf)`
2. 遍历左子树时，上界变为当前节点值
3. 遍历右子树时，下界变为当前节点值
4. 只要当前值不在合法区间内，立即返回 `False`

#### 代码
```python
class Solution:
    def isValidBST(self, root):
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float("-inf"), float("inf"))
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(h)**

---

## 四、第 101 题详解 — 对称二叉树

### 题目描述
给定一个二叉树的根节点 `root`，判断它是否轴对称。

### 示例
- `root = [1,2,2,3,4,4,3]` -> `true`
- `root = [1,2,2,null,3,null,3]` -> `false`

### 核心思路：同时检查镜像位置

判断一棵树是否对称，本质上是在判断左子树和右子树是否互为镜像。

镜像条件：
- 两个节点都为空，成立
- 一个为空一个不为空，不成立
- 值必须相等
- `left.left` 对应 `right.right`
- `left.right` 对应 `right.left`

#### 代码
```python
class Solution:
    def isSymmetric(self, root):
        def check(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return check(left.left, right.right) and check(left.right, right.left)

        return check(root.left, root.right) if root else True
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(h)**

---

## 五、第 102 题详解 — 二叉树的层序遍历

### 题目描述
给你二叉树的根节点 `root`，返回其节点值的层序遍历结果。

### 示例
- `root = [3,9,20,null,null,15,7]` -> `[[3],[9,20],[15,7]]`

### 核心思路：队列做 BFS

层序遍历天然适合用队列。

#### 步骤
1. 根节点入队
2. 每次先记录当前层节点数 `len(queue)`
3. 这一轮循环只弹出当前层的节点
4. 把下一层节点加入队列

#### 代码
```python
from collections import deque


class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        ans = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)

        return ans
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(n)**

---

## 六、第 104 题详解 — 二叉树的最大深度

### 题目描述
给定一个二叉树，返回其最大深度。

### 示例
- `root = [3,9,20,null,null,15,7]` -> `3`

### 核心思路：递归定义深度

一棵树的最大深度等于：

`max(左子树深度, 右子树深度) + 1`

这是最基础的树递归定义题。

#### 代码
```python
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(h)**

---

## 七、第 105 题详解 — 从前序与中序遍历序列构造二叉树

### 题目描述
给定前序遍历 `preorder` 和中序遍历 `inorder`，构造并返回二叉树。

### 示例
- `preorder = [3,9,20,15,7]`
- `inorder = [9,3,15,20,7]`
- 返回对应二叉树根节点

### 核心思路：前序定根，中序划分左右子树

#### 关键性质
- 前序遍历第一个元素一定是当前子树的根
- 在中序遍历中，根节点左边是左子树，右边是右子树

为了避免每次在线性扫描 `inorder` 中找根节点位置，可以先建一个哈希表。

#### 代码
```python
class Solution:
    def buildTree(self, preorder, inorder):
        index = {value: i for i, value in enumerate(inorder)}

        def dfs(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r:
                return None

            root_val = preorder[pre_l]
            root = TreeNode(root_val)
            pivot = index[root_val]
            left_size = pivot - in_l

            root.left = dfs(pre_l + 1, pre_l + left_size, in_l, pivot - 1)
            root.right = dfs(pre_l + left_size + 1, pre_r, pivot + 1, in_r)
            return root

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(n)**

---

## 八、第 108 题详解 — 将有序数组转换为二叉搜索树

### 题目描述
给你一个升序整数数组 `nums`，将其转换为一棵高度平衡的二叉搜索树。

### 示例
- `nums = [-10,-3,0,5,9]`

### 核心思路：每次取中点做根

为了尽量平衡，每一层都选择中间位置作为根节点：
- 左半段构造左子树
- 右半段构造右子树

这是一道典型的分治题。

#### 代码
```python
class Solution:
    def sortedArrayToBST(self, nums):
        def dfs(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, len(nums) - 1)
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(log n)** 到 **O(n)**，取决于树形和递归栈

---

## 九、第 114 题详解 — 二叉树展开为链表

### 题目描述
给你二叉树的根节点 `root`，请你将它展开为一个单链表。

展开后要求：
- 使用 `right` 指针串联节点
- 顺序与前序遍历一致
- `left` 指针全部置空

### 示例
- `root = [1,2,5,3,4,null,6]`
- 展开后为 `1 -> 2 -> 3 -> 4 -> 5 -> 6`

### 核心思路：后序调整指针

先分别处理左右子树，再把左子树整体插到右边。

#### 步骤
1. 递归展开左子树和右子树
2. 若左子树存在，把它接到当前节点右边
3. 原来的右子树挂到左子树展开后的尾部
4. 返回当前展开链表的尾节点

#### 代码
```python
class Solution:
    def flatten(self, root):
        def dfs(node):
            if not node:
                return None

            left_tail = dfs(node.left)
            right_tail = dfs(node.right)

            if node.left:
                tail = left_tail
                tail.right = node.right
                node.right = node.left
                node.left = None

            return right_tail or left_tail or node

        dfs(root)
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(h)**

---

## 十、第 124 题详解 — 二叉树中的最大路径和

### 题目描述
路径被定义为一条从任意节点出发，沿父子关系连接到任意节点的序列。同一个节点不能重复经过。

求这棵二叉树中的最大路径和。

### 示例
- `root = [1,2,3]` -> `6`
- `root = [-10,9,20,null,null,15,7]` -> `42`

### 核心思路：树形 DP

这题的难点在于：
- 返回给父节点的值，不能同时取左右两边
- 但统计答案时，可以把当前节点作为拐点，同时接左边和右边

#### 定义
对于每个节点：
- `dfs(node)` 返回“从当前节点向下延伸时，能提供给父节点的最大贡献值”
- 当前节点作为路径最高点时，路径和为：
  `node.val + max(0, left) + max(0, right)`

#### 代码
```python
class Solution:
    def maxPathSum(self, root):
        ans = float("-inf")

        def dfs(node):
            nonlocal ans
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            ans = max(ans, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return ans
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(h)**

---

## 十一、第 199 题详解 — 二叉树的右视图

### 题目描述
给定一个二叉树的根节点 `root`，返回从右侧所能看到的节点值。

### 示例
- `root = [1,2,3,null,5,null,4]` -> `[1,3,4]`

### 核心思路：每层取最后一个节点

使用层序遍历时，每一层最后被处理到的节点，就是这一层右侧能看到的节点。

#### 代码
```python
from collections import deque


class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        ans = []
        queue = deque([root])

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == size - 1:
                    ans.append(node.val)

        return ans
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(n)**

---

## 十二、第 226 题详解 — 翻转二叉树

### 题目描述
翻转一棵二叉树，交换每个节点的左右子树。

### 示例
- `root = [4,2,7,1,3,6,9]` -> `[4,7,2,9,6,3,1]`

### 核心思路：遍历每个节点并交换左右指针

不管是前序、后序还是层序，本质都是：
- 访问到当前节点
- 交换 `left` 和 `right`

递归写法最简洁。

#### 代码
```python
class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(h)**

---

## 十三、第 230 题详解 — 二叉搜索树中第 K 小的元素

### 题目描述
给定一棵二叉搜索树和一个整数 `k`，返回其中第 `k` 小的元素值。

### 示例
- `root = [3,1,4,null,2], k = 1` -> `1`

### 核心思路：BST 中序遍历天然有序

BST 的中序遍历结果是递增序列，因此只要中序遍历到第 `k` 个节点即可。

#### 代码
```python
class Solution:
    def kthSmallest(self, root, k):
        stack = []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
```

#### 复杂度
- 时间复杂度：**O(h + k)**，最坏为 **O(n)**
- 空间复杂度：**O(h)**

---

## 十四、第 235 题详解 — 二叉搜索树的最近公共祖先

### 题目描述
给定一棵二叉搜索树，找到两个指定节点 `p` 和 `q` 的最近公共祖先。

### 示例
- `root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8` -> `6`
- `root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4` -> `2`

### 核心思路：利用 BST 的大小关系

二叉搜索树满足：
- 左子树所有节点值小于当前节点
- 右子树所有节点值大于当前节点

因此从根节点开始：
- 如果 `p` 和 `q` 都小于当前节点，最近公共祖先在左子树
- 如果 `p` 和 `q` 都大于当前节点，最近公共祖先在右子树
- 否则当前节点就是分叉点，也就是最近公共祖先

#### 代码
```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        low = min(p.val, q.val)
        high = max(p.val, q.val)

        while root:
            if high < root.val:
                root = root.left
            elif low > root.val:
                root = root.right
            else:
                return root
```

#### 复杂度
- 时间复杂度：**O(h)**，`h` 为树高
- 空间复杂度：**O(1)**

---

## 十五、第 236 题详解 — 二叉树的最近公共祖先

### 题目描述
给定一棵二叉树，找到两个指定节点 `p` 和 `q` 的最近公共祖先。

### 示例
- `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1` -> `3`

### 核心思路：分治递归

#### 递归含义
函数返回值表示：
- 当前子树中若找到了 `p` 或 `q`，返回对应节点
- 若左右子树分别找到了一个目标节点，则当前节点就是最近公共祖先

#### 代码
```python
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left or right
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(h)**

---

## 十六、第 437 题详解 — 路径总和 III

### 题目描述
给定一个二叉树和一个整数 `targetSum`，统计路径和等于目标值的路径数量。

要求：
- 路径方向必须向下
- 不要求从根开始
- 不要求在叶子结束

### 示例
- `root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8` -> `3`

### 核心思路：前缀和 + DFS

与数组前缀和类似：
- 设从根到当前节点的路径和为 `curr`
- 若之前出现过前缀和 `curr - targetSum`
- 说明从那个位置之后到当前节点的路径和恰好为目标值

#### 关键点
1. 用哈希表记录前缀和出现次数
2. 进入子树前先加入当前前缀和
3. 回溯时要减掉当前前缀和，避免影响兄弟分支

#### 代码
```python
from collections import defaultdict


class Solution:
    def pathSum(self, root, targetSum):
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(node, curr):
            if not node:
                return 0

            curr += node.val
            count = prefix[curr - targetSum]
            prefix[curr] += 1

            count += dfs(node.left, curr)
            count += dfs(node.right, curr)

            prefix[curr] -= 1
            return count

        return dfs(root, 0)
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(n)**

---

## 十七、第 543 题详解 — 二叉树的直径

### 题目描述
给定一棵二叉树，返回其直径长度。

直径定义为任意两个节点之间最长路径的边数。

### 示例
- `root = [1,2,3,4,5]` -> `3`

### 核心思路：深度计算过程中顺手更新答案

对于每个节点：
- 左子树最大深度是 `left`
- 右子树最大深度是 `right`
- 经过当前节点的最长路径长度就是 `left + right`

遍历所有节点取最大值即可。

#### 代码
```python
class Solution:
    def diameterOfBinaryTree(self, root):
        ans = 0

        def depth(node):
            nonlocal ans
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)
            ans = max(ans, left + right)
            return max(left, right) + 1

        depth(root)
        return ans
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(h)**

---

## 十八、第 617 题详解 — 合并二叉树

### 题目描述
给你两棵二叉树 `root1` 和 `root2`，请你将它们合并成一棵新二叉树。

合并规则是：
- 如果两个节点都存在，就把节点值相加
- 如果只有一个节点存在，就直接使用该节点

### 示例
- `root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]` -> `[3,4,5,5,4,null,7]`
- `root1 = [1], root2 = [1,2]` -> `[2,2]`

### 核心思路：同步递归合并两棵树

递归函数同时接收两棵树的当前节点：
- 如果一边为空，直接返回另一边
- 如果两边都存在，就把值相加
- 然后继续递归处理左右子树

这类题本质上是在做“两棵树的同步 DFS”。

#### 代码
```python
class Solution:
    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1

        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
```

#### 复杂度
- 时间复杂度：**O(min(m, n))** 到 **O(m + n)**，取决于重叠节点数量
- 空间复杂度：**O(h)**，`h` 为递归深度

---

## 十九、第 96 题详解 — 不同的二叉搜索树

### 题目描述
给定一个整数 `n`，求由 `1...n` 组成且结构互不相同的二叉搜索树有多少种。

### 示例
- `n = 3` -> `5`
- `n = 1` -> `1`

### 核心思路：枚举根节点做区间划分

如果选择某个数 `root` 作为根节点：
- 左子树有 `root - 1` 个节点
- 右子树有 `n - root` 个节点

因此：

`dp[nodes] += dp[left_size] * dp[right_size]`

#### 代码
```python
class Solution:
    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                dp[nodes] += dp[root - 1] * dp[nodes - root]

        return dp[n]
```

#### 复杂度
- 时间复杂度：**O(n^2)**
- 空间复杂度：**O(n)**

---

## 二十、第 297 题详解 — 二叉树的序列化与反序列化

### 题目描述
设计一个算法，实现二叉树的序列化与反序列化。

### 核心思路：先序遍历记录空节点

序列化时：
- 遇到空节点用 `#` 表示
- 按先序顺序写入字符串

反序列化时：
- 按同样顺序递归读回
- 遇到 `#` 就返回空节点

#### 代码
```python
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
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(n)**

---

## 二十一、第 337 题详解 — 打家劫舍 III

### 题目描述
给定一棵二叉树，每个节点代表一间房屋。相邻节点不能同时被偷，求可偷到的最大金额。

### 示例
- `root = [3,2,3,null,3,null,1]` -> `7`
- `root = [3,4,5,1,3,null,1]` -> `9`

### 核心思路：树形 DP 记录“偷”与“不偷”

对于每个节点，返回两个值：
- `rob_current`：偷当前节点时的最大收益
- `skip_current`：不偷当前节点时的最大收益

这样父节点就能据此做选择。

#### 代码
```python
class Solution:
    def rob(self, root):
        def dfs(node):
            if not node:
                return 0, 0

            left = dfs(node.left)
            right = dfs(node.right)
            rob_current = node.val + left[1] + right[1]
            skip_current = max(left) + max(right)
            return rob_current, skip_current

        return max(dfs(root))
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(h)**

---

## 二十二、第 538 题详解 — 把二叉搜索树转换为累加树

### 题目描述
给定一棵二叉搜索树，将其转换为累加树，使每个节点的新值等于所有大于等于它的节点值之和。

### 示例
- `root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]`
- 转换后为 `[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]`

### 核心思路：反向中序遍历累加

BST 的中序遍历是从小到大，所以要从大到小累加，就做：
- 右子树
- 当前节点
- 左子树

#### 代码
```python
class Solution:
    def convertBST(self, root):
        total = 0

        def dfs(node):
            nonlocal total
            if not node:
                return
            dfs(node.right)
            total += node.val
            node.val = total
            dfs(node.left)

        dfs(root)
        return root
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(h)**

---

## 二十三、第 110 题详解 — 平衡二叉树

### 题目描述
给定一个二叉树，判断它是否是高度平衡的二叉树。

平衡条件是：
- 每个节点的左右子树高度差不超过 `1`

### 示例
- `root = [3,9,20,null,null,15,7]` -> `True`
- `root = [1,2,2,3,3,null,null,4,4]` -> `False`

### 核心思路：自底向上返回高度，失衡时提前剪枝

递归函数返回当前子树高度。

但如果某棵子树已经失衡，就直接返回 `-1`：
- 这样上层节点一看到 `-1`
- 就不用继续正常计算高度
- 可以立刻判定整棵树不平衡

#### 代码
```python
class Solution:
    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            if left == -1:
                return -1

            right = height(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return height(root) != -1
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(h)**

---

## 二十四、二叉树专题总结

这些题可以按模板归类：

| 类型 | 对应题目 | 关键方法 |
|------|----------|----------|
| 基础遍历 | 94、102、199、230、538 | DFS、BFS、中序 |
| 树性质判断 | 98、101、110 | 区间递归、镜像递归、树高判断 |
| 递归构造 | 105、108、297 | 分治、哈希定位 |
| 指针调整 | 114、226、617 | 原地修改树结构 |
| 路径与祖先 | 235、236、437 | BST 性质、分治、前缀和 |
| 树形 DP | 96、124、337、543 | 定义递归返回值 |
| 基础深度题 | 104 | 树高递归 |

建议复习顺序：
1. 先掌握前中后序和层序遍历
2. 再练“递归函数返回什么”这一类题
3. 最后集中突破树形 DP 和构造类题目
