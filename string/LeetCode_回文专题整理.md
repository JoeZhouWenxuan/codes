# LeetCode 回文专题整理

## 一、回文题总览

回文题是 LeetCode 里非常高频的一条主线，常见做法主要集中在：
- 双指针
- 中心扩展
- 动态规划
- 回溯
- KMP / 字符串构造

---

## 二、按题型分类

### 1. 回文判断类

| 题号 | 题目 | 目录 | 核心方法 |
|------|------|------|----------|
| 9 | 回文数 | `string` | 转字符串 / 数学反转 |
| 125 | 验证回文串 | `string` | 双指针 |
| 680 | 验证回文串 II | `string` | 双指针 + 容错一次删除 |
| 234 | 回文链表 | `linked_list` | 快慢指针 + 反转链表 |

---

### 2. 回文子串类

| 题号 | 题目 | 目录 | 核心方法 |
|------|------|------|----------|
| 5 | 最长回文子串 | `string` | 中心扩展 / Manacher |
| 647 | 回文子串 | `string` | 中心扩展 |

这类题的关键点是：
- “子串”必须连续
- 中心扩展通常是最自然的解法

---

### 3. 回文分割类

| 题号 | 题目 | 目录 | 核心方法 |
|------|------|------|----------|
| 131 | 分割回文串 | `string` / `backtracking` | 回溯 + 回文判断 |
| 132 | 分割回文串 II | `string` | DP + 回文预处理 |

这类题的关键点是：
- 先判断一段是不是回文
- 再决定怎么切分

---

### 4. 回文子序列类

| 题号 | 题目 | 目录 | 核心方法 |
|------|------|------|----------|
| 516 | 最长回文子序列 | `string` | 区间 DP |

这类题和子串不同：
- “子序列”不要求连续
- 常见做法是二维 DP

---

### 5. 回文构造类

| 题号 | 题目 | 目录 | 核心方法 |
|------|------|------|----------|
| 214 | 最短回文串 | `string` | KMP / 最长回文前缀 |
| 409 | 最长回文串 | `string` | 贪心 + 计数 |

---

## 三、推荐刷题顺序

建议这样刷：

1. `125` 验证回文串
2. `680` 验证回文串 II
3. `647` 回文子串
4. `5` 最长回文子串
5. `409` 最长回文串
6. `131` 分割回文串
7. `132` 分割回文串 II
8. `516` 最长回文子序列
9. `214` 最短回文串
10. `234` 回文链表

---

## 四、常见易混点

1. `子串` 要连续，`子序列` 不要求连续。
2. `5` 和 `647` 都适合中心扩展，但一个求最长长度，一个求总个数。
3. `131` 是枚举所有方案，`132` 是求最优解，所以要用 DP。
4. `409` 不是判断原串是否回文，而是问这些字符最多能拼成多长的回文串。
5. `214` 的难点在于找到“最长回文前缀”，它不是普通双指针能高效解决的。

---

## 五、仓库内对应文件

- [5_longest_palindromic_substring.py](/Users/bytedance/Documents/codes/string/5_longest_palindromic_substring.py)
- [9_palindrome_number.py](/Users/bytedance/Documents/codes/string/9_palindrome_number.py)
- [125_valid_palindrome.py](/Users/bytedance/Documents/codes/string/125_valid_palindrome.py)
- [131_palindrome_partitioning.py](/Users/bytedance/Documents/codes/string/131_palindrome_partitioning.py)
- [132_palindrome_partitioning_ii.py](/Users/bytedance/Documents/codes/string/132_palindrome_partitioning_ii.py)
- [214_shortest_palindrome.py](/Users/bytedance/Documents/codes/string/214_shortest_palindrome.py)
- [409_longest_palindrome.py](/Users/bytedance/Documents/codes/string/409_longest_palindrome.py)
- [516_longest_palindromic_subsequence.py](/Users/bytedance/Documents/codes/string/516_longest_palindromic_subsequence.py)
- [647_palindromic_substrings.py](/Users/bytedance/Documents/codes/string/647_palindromic_substrings.py)
- [680_valid_palindrome_ii.py](/Users/bytedance/Documents/codes/string/680_valid_palindrome_ii.py)
- [234_palindrome_linked_list.py](/Users/bytedance/Documents/codes/linked_list/234_palindrome_linked_list.py)
