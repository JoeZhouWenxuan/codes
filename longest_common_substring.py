class Solution:
    def longest_common_substring(self, s1, s2):
        n = len(s1)
        m = len(s2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        max_len = 0
        end_pos = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        end_pos = j - 1
                else:
                    dp[i][j] = 0

        sub_string = "" if max_len == 0 else s2[end_pos - max_len + 1: end_pos + 1]
        return max_len, sub_string
    

if __name__ == "__main__":
    print(Solution().longest_common_substring('1234', '23'))
