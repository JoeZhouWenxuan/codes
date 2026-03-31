# LeetCode 栈专题题解

## 一、stack 目录 — 栈专题

本文把 LeetCode 中常见的栈题集中整理，方便按“括号匹配、单调栈、设计栈结构”来复习。

| 题号 | 题目 | 难度 | 核心标签 |
|------|------|------|----------|
| 155 | 最小栈 | 中等 | 栈设计、辅助栈 |

---

## 二、第 155 题详解 — 最小栈

### 题目描述
设计一个支持 `push`、`pop`、`top`，并且能够在 `O(1)` 时间返回最小值的栈。

### 核心思路：主栈 + 辅助最小栈

维护两个栈：
- `stack`：正常存所有元素
- `min_stack`：记录到当前位置为止的最小值

这样每次：
- `push` 时把当前最小值同步压入 `min_stack`
- `pop` 时两个栈一起弹出
- `getMin` 直接返回 `min_stack` 栈顶

#### 代码
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
```

#### 复杂度
- `push`：**O(1)**
- `pop`：**O(1)**
- `top`：**O(1)**
- `getMin`：**O(1)**
