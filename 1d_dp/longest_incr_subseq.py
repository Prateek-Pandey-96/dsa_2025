from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        lis = [1]*n
        ans = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and lis[i] < lis[j]+1:
                    lis[i] = lis[j] + 1
            ans = max(ans, lis[i])

        return ans
        
