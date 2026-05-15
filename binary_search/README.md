# Binary Search

本目录整理了 LeetCode 中常见的二分查找题目，采用“每题一个 `.py` 文件”的形式。

题解总表：
- [LeetCode_二分查找专题题解.md](/Users/bytedance/Documents/codes/binary_search/LeetCode_二分查找专题题解.md)

已整理文件：
- [4_median_of_two_sorted_arrays.py](/Users/bytedance/Documents/codes/binary_search/4_median_of_two_sorted_arrays.py)
- [33_search_in_rotated_sorted_array.py](/Users/bytedance/Documents/codes/binary_search/33_search_in_rotated_sorted_array.py)
- [34_find_first_and_last_position.py](/Users/bytedance/Documents/codes/binary_search/34_find_first_and_last_position.py)
- [35_search_insert_position.py](/Users/bytedance/Documents/codes/binary_search/35_search_insert_position.py)
- [74_search_a_2d_matrix.py](/Users/bytedance/Documents/codes/binary_search/74_search_a_2d_matrix.py)
- [153_find_minimum_in_rotated_sorted_array.py](/Users/bytedance/Documents/codes/binary_search/153_find_minimum_in_rotated_sorted_array.py)
- [240_Search_a_2D_Matrix_II.py](/Users/bytedance/Documents/codes/binary_search/240_Search_a_2D_Matrix_II.py)


## 二分查找啥时候<=，啥时候<
判断 `while left <= right` 还是 `while left < right`，核心看一句话：
> 搜索区间里，`right` 是不是一个合法候选位置。
如果你定义的是 **闭区间**：
```python
[left, right]
```
那 `left` 和 `right` 都可能是答案，所以循环条件用：
```python
while left <= right:
```
因为 `left == right` 时，区间里还有一个元素没检查。
典型写法：
```python
left, right = 0, len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```
比如普通二分查找、搜索旋转数组，通常用这个。
如果你定义的是 **左闭右开区间**：

```python
[left, right)
```
那 `right` 不是合法候选位置，所以循环条件用：
```python
while left < right:
```
因为 `left == right` 时，区间为空了。
典型写法：
```python
left, right = 0, len(nums)

while left < right:
    mid = (left + right) // 2

    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid
```
常用于找左边界、插入位置，比如 `bisect_left`。
一个好记法：
```python
right = len(nums) - 1  -> while left <= right
right = len(nums)      -> while left < right
```
还有一种常见场景：找某个边界/最小满足条件的值，也常用 `<`：
```python
left, right = 0, n - 1

while left < right:
    mid = (left + right) // 2

    if check(mid):
        right = mid
    else:
        left = mid + 1

return left
```
这里虽然初始是 `[left, right]` 闭区间，但用 `while left < right`，因为它不是在找“等于 target 的某个元素”，而是在不断缩小答案范围，最后让 `left == right` 收敛到答案。
所以更完整地说：
- **查找某个具体值**：常用 `while left <= right`
- **找边界 / 最小满足条件 / 最大满足条件**：常用 `while left < right`
- **右边界初始化为 `len(nums) - 1`**：一般配 `<=`
- **右边界初始化为 `len(nums)`**：一般配 `<`

题 `4. 寻找两个正序数组的中位数`，是在找一个合法划分点，划分点可能在 `0` 或 `m`，所以用闭区间：

```python
left, right = 0, m
while left <= right:
```

因为 `i = 0` 和 `i = m` 都是合法候选划分。