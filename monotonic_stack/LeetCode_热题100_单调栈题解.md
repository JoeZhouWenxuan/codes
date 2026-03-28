# LeetCode 热题 100 单调栈专题整理

## 一、monotonic_stack 目录 — 单调栈专题

本文参考仓库内 `binary_tree` 目录的整理方式，归纳 LeetCode 热题 100 中常见的单调栈题目。

| 题号 | 题目 | 难度 | 核心标签 |
|------|------|------|----------|
| 42 | 接雨水 | 困难 | 单调栈、按层计算 |
| 84 | 柱状图中最大的矩形 | 困难 | 单调栈、找左右边界 |
| 85 | 最大矩形 | 困难 | 单调栈、矩阵转柱状图 |
| 739 | 每日温度 | 中等 | 单调递减栈、下一个更大元素 |

---

## 二、第 42 题详解 — 接雨水

### 题目描述
给定若干柱子的高度数组 `height`，计算下雨之后最多能接多少雨水。

### 示例
- `height = [0,1,0,2,1,0,1,3,2,1,2,1]` -> `6`
- `height = [4,2,0,3,2,5]` -> `9`

### 核心思路：单调递减栈找凹槽

栈中存下标，并保持对应高度单调递减。

当当前柱子比栈顶更高时，说明出现了一个“凹槽底部”：
- 栈顶元素是凹槽底
- 当前元素是右边界
- 新的栈顶是左边界

这样就能计算这一层能接的雨水面积。

#### 代码
```python
class Solution:
    def trap(self, height):
        stack = []
        ans = 0

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                width = i - left - 1
                bounded_height = min(height[left], h) - height[bottom]
                ans += width * bounded_height
            stack.append(i)

        return ans
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(n)**

---

## 三、第 84 题详解 — 柱状图中最大的矩形

### 题目描述
给定柱状图每一列的高度 `heights`，求其中最大的矩形面积。

### 示例
- `heights = [2,1,5,6,2,3]` -> `10`
- `heights = [2,4]` -> `4`

### 核心思路：单调递增栈确定每根柱子的扩展范围

对于每根柱子，我们希望知道：
- 左边第一个比它矮的位置
- 右边第一个比它矮的位置

这样就能把当前柱子作为矩形高度，计算它能扩展出的最大宽度。

单调递增栈可以在一次遍历中完成这件事。为了让栈中剩余元素也能被结算，可以在数组末尾补一个 `0`。

#### 代码
```python
class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        ans = 0
        extended = heights + [0]

        for i, h in enumerate(extended):
            while stack and extended[stack[-1]] > h:
                height = extended[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                ans = max(ans, height * width)
            stack.append(i)

        return ans
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(n)**

---

## 四、第 85 题详解 — 最大矩形

### 题目描述
给定一个仅包含 `0` 和 `1` 的二维矩阵，找出只包含 `1` 的最大矩形面积。

### 示例
- `matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]` -> `6`
- `matrix = [["0"]]` -> `0`

### 核心思路：逐行累积高度，转成柱状图问题

这题的关键是把二维矩阵转化为多个“一维柱状图”。

对于每一行：
- 如果当前位置是 `1`，就把这一列高度加一
- 如果当前位置是 `0`，这一列高度清零

这样每处理完一行，就得到一个新的柱状图。然后直接复用第 84 题“柱状图中最大的矩形”的单调栈解法，更新答案即可。

#### 代码
```python
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        ans = 0

        for row in matrix:
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max(ans, self.largestRectangleArea(heights))

        return ans
```

#### 复杂度
- 时间复杂度：**O(m x n)**
- 空间复杂度：**O(n)**

---

## 五、第 739 题详解 — 每日温度

### 题目描述
给定每日温度数组 `temperatures`，返回每一天距离下一个更高温度还要等几天。

### 示例
- `temperatures = [73,74,75,71,69,72,76,73]` -> `[1,1,4,2,1,1,0,0]`
- `temperatures = [30,40,50,60]` -> `[1,1,1,0]`

### 核心思路：单调递减栈维护未找到答案的下标

栈里存的是下标，并保持对应温度单调递减。

当遍历到当前温度 `temp` 时：
- 如果它比栈顶下标对应的温度更高
- 就说明栈顶那一天找到了下一个更暖和的日子
- 两个下标之差就是等待天数

#### 代码
```python
class Solution:
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)

        return ans
```

#### 复杂度
- 时间复杂度：**O(n)**
- 空间复杂度：**O(n)**
