# 79. 单词搜索
# https://leetcode.cn/problems/word-search/
# 难度：中等
#
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word。
# 如果 word 存在于网格中，返回 true；否则，返回 false。
#
# 示例：
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"    输出：True
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"      输出：False

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    #     rows, cols = len(board), len(board[0])

    #     def dfs(i: int, j: int, k: int) -> bool:
    #         if board[i][j] != word[k]:
    #             return False
    #         if k == len(word) - 1:
    #             return True

    #         char = board[i][j]
    #         board[i][j] = "#"
    #         for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    #             ni, nj = i + di, j + dj
    #             if 0 <= ni < rows and 0 <= nj < cols and board[ni][nj] != "#":
    #                 if dfs(ni, nj, k + 1):
    #                     board[i][j] = char
    #                     return True
    #         board[i][j] = char
    #         return False

    #     for i in range(rows):
    #         for j in range(cols):
    #             if dfs(i, j, 0):
    #                 return True

    #     return False
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word):
                return True
            ch = board[i][j]
            board[i][j] = '#'
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and board[i][j] != '#':
                    if dfs(ni, nj, k+1):
                        board[i][j] = ch
                        return True
            board[i][j] = ch
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False

        
if __name__ == "__main__":
    s = Solution()
    print(
        s.exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
        )
    )  # True
    print(
        s.exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCB",
        )
    )  # False
