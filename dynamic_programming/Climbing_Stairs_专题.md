# 爬楼梯模型专题

## 一、核心模型

爬楼梯类题的共同点是：

```python
到达当前位置的答案 = 从若干个前置位置转移过来
```

最经典的 `70. 爬楼梯`：

```python
dp[i] = dp[i - 1] + dp[i - 2]
```

含义是到达第 `i` 阶，最后一步可能来自：
- 第 `i - 1` 阶，走 1 步
- 第 `i - 2` 阶，走 2 步

---

## 二、相关题目

| 题号 | 题目 | 类型 | 状态转移 |
|------|------|------|----------|
| 509 | 斐波那契数 | 基础递推 | `fib[i] = fib[i - 1] + fib[i - 2]` |
| 70 | 爬楼梯 | 方案数 | `dp[i] = dp[i - 1] + dp[i - 2]` |
| 746 | 使用最小花费爬楼梯 | 最小代价 | `dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])` |
| 1137 | 第 N 个泰波那契数 | 三步递推 | `dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]` |
| 377 | 组合总和 IV | 任意步长方案数 | `dp[i] += dp[i - num]` |

---

## 三、代码索引

- [509_Fibonacci_Number.py](./509_Fibonacci_Number.py)
- [70_Climbing_Stairs.py](./70_Climbing_Stairs.py)
- [746_Min_Cost_Climbing_Stairs.py](./746_Min_Cost_Climbing_Stairs.py)
- [1137_N-th_Tribonacci_Number.py](./1137_N-th_Tribonacci_Number.py)
- [377_Combination_Sum_IV.py](./377_Combination_Sum_IV.py)

---

## 四、常见变化

### 1. 求方案数

通常用加法：

```python
dp[i] = dp[i - 1] + dp[i - 2]
```

### 2. 求最小代价

通常用 `min`：

```python
dp[i] = min(来自上一步的代价, 来自上两步的代价)
```

### 3. 可走步长变多

如果每次可以走 `1、2、3` 阶：

```python
dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
```

如果步长来自数组 `nums`：

```python
for total in range(1, target + 1):
    for num in nums:
        if total >= num:
            dp[total] += dp[total - num]
```

