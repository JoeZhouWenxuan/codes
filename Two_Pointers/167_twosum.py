class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]
    print(Solution().twoSum([2, 3, 4], 6))       # Output: [1, 3]
    print(Solution().twoSum([-1, 0], -1))        # Output: [1, 2]