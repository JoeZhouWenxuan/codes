from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # nums[i] > 0: all remaining elements are positive, no solution possible
            if nums[i] > 0:
                break
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            # Even with the two largest elements, sum is still < 0, skip this i
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
    

if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
    print(Solution().threeSum([]))                     # []
    print(Solution().threeSum([0]))                    # []
    print(Solution().threeSum([-1, 0, 1, 2]))          # [[-1, 0, 1]] (would have been [] with the bug)