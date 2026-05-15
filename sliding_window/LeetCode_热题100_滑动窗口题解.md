# LeetCode 热题 100 滑动窗口专题整理

## 一、专题总览

滑动窗口适合处理“连续子数组 / 连续子串”问题。核心是用两个指针维护一个窗口 `[left, right]`，右指针负责扩张，左指针负责收缩。

| 题号 | 题目 | 难度 | 类型 | 当前代码 |
|------|------|------|------|----------|
| 3 | 无重复字符的最长子串 | 中等 | 可变窗口、去重 | [`3_Longest_Substring_Without_Repeating_Characters.py`](./3_Longest_Substring_Without_Repeating_Characters.py) |
| 438 | 找到字符串中所有字母异位词 | 中等 | 固定窗口、字符计数 | [`438_Find_All_Anagrams_in_a_String.py`](./438_Find_All_Anagrams_in_a_String.py) |
| 76 | 最小覆盖子串 | 困难 | 可变窗口、覆盖计数 | [`76_Minimum_Window_Substring.py`](./76_Minimum_Window_Substring.py) |
| 239 | 滑动窗口最大值 | 困难 | 固定窗口、单调队列 | [`239_Sliding_Window_Maximum.py`](./239_Sliding_Window_Maximum.py) |
| 560 | 和为 K 的子数组 | 中等 | 前缀和、哈希表 | [`560_Subarray_Sum_Equals_K.py`](./560_Subarray_Sum_Equals_K.py) |

说明：`560` 经常被放在连续子数组专题里，但它不是普通滑动窗口。因为数组里可能有负数，窗口和不会单调变化，所以要用“前缀和 + 哈希表”。

---

## 二、滑动窗口模板

### 1. 可变窗口模板

适合“最长 / 最短满足条件的连续区间”。

```python
left = 0
ans = 初始值

for right, x in enumerate(nums):
    # 1. 右指针扩张，把 x 加入窗口

    while 窗口不满足条件 或 窗口已经满足条件需要尝试收缩:
        # 2. 根据题意更新答案
        # 3. 移除 nums[left]
        left += 1

    # 4. 根据题意更新答案
```

常见题目：
- `3. 无重复字符的最长子串`
- `76. 最小覆盖子串`

---

### 2. 固定窗口模板

适合窗口长度固定的问题，比如长度必须等于 `len(p)`。

```python
left = 0

for right, x in enumerate(nums):
    # 1. 加入右侧元素

    if right - left + 1 > window_size:
        # 2. 移除左侧元素
        left += 1

    if right - left + 1 == window_size:
        # 3. 判断当前窗口是否符合要求
```

常见题目：
- `438. 找到字符串中所有字母异位词`
- `239. 滑动窗口最大值`

---

## 三、第 3 题：无重复字符的最长子串

### 核心思路

维护一个没有重复字符的窗口：
- `right` 向右扩张
- 如果遇到重复字符，就移动 `left`
- 每次窗口合法时更新最大长度

### 状态

```python
last_seen[ch] = 字符 ch 上一次出现的位置
left = 当前窗口左边界
```

### 关键点

```python
if ch in last_seen and last_seen[ch] >= left:
    left = last_seen[ch] + 1
```

必须判断 `last_seen[ch] >= left`，避免把左边界往回拉。

---

## 四、第 438 题：找到字符串中所有字母异位词

### 核心思路

异位词长度固定为 `len(p)`，所以可以维护固定长度窗口。

### 状态

```python
need = Counter(p)
window = 当前窗口里的字符计数
```

当窗口长度超过 `len(p)` 时，左侧字符出窗口。每次窗口长度等于 `len(p)` 时，比较 `window == need`。

### 关键点

这是固定窗口题，窗口大小不能无限扩张。

---

## 五、第 76 题：最小覆盖子串

### 核心思路

窗口需要覆盖 `t` 中所有字符：
- 右指针扩张，直到窗口满足覆盖条件
- 满足后不断移动左指针，尝试缩短窗口
- 一旦移走关键字符导致不满足，再继续扩张右指针

### 状态

```python
counts = Counter(t)
remain = 还没有满足要求的字符种数
```

当某个字符数量刚好满足时：

```python
counts[ch] == 0
remain -= 1
```

当左指针移走字符后，该字符又不够了：

```python
counts[left_char] > 0
remain += 1
```

### 关键点

`remain == 0` 表示当前窗口已经覆盖 `t`，此时要尽量收缩左边界。

---

## 六、第 239 题：滑动窗口最大值

### 核心思路

普通滑动窗口无法快速知道窗口最大值，需要使用单调队列。

队列中存下标，并保持对应值从队头到队尾递减：
- 队头永远是当前窗口最大值
- 新元素进来时，把队尾所有比它小的元素弹出
- 如果队头下标已经滑出窗口，就弹出队头

### 典型代码

```python
from collections import deque

def maxSlidingWindow(nums, k):
    q = deque()
    ans = []

    for i, x in enumerate(nums):
        while q and nums[q[-1]] <= x:
            q.pop()
        q.append(i)

        if q[0] <= i - k:
            q.popleft()

        if i >= k - 1:
            ans.append(nums[q[0]])

    return ans
```

---

## 七、第 560 题：和为 K 的子数组

### 为什么不是普通滑动窗口

如果数组里有负数，窗口和不具备单调性：
- 右指针右移，和可能变大，也可能变小
- 左指针右移，和也可能变大或变小

所以不能靠“和大了就收缩，和小了就扩张”来保证正确。

### 正确思路

用前缀和：

```python
prefix[j] - prefix[i] = k
```

遍历到当前前缀和 `prefix` 时，只需要知道之前出现过多少次 `prefix - k`。

---

## 八、推荐刷题顺序

1. `3. 无重复字符的最长子串`
2. `438. 找到字符串中所有字母异位词`
3. `76. 最小覆盖子串`
4. `239. 滑动窗口最大值`
5. `560. 和为 K 的子数组`

---

## 九、判断方法

看到题目时可以先问三件事：

1. 是否要求连续子数组或连续子串？
2. 窗口长度是固定的，还是满足条件后可以收缩？
3. 窗口状态是否具有单调性？

如果答案是“连续 + 可用左右指针维护状态”，大概率是滑动窗口。

如果数组有负数，且题目问“和为 K 的子数组个数”，优先考虑前缀和而不是滑动窗口。
