from typing import List

class Solution:
    def dfs(self, idx: int, nums: List[int], target: int, dp: List[int]) -> bool:
        if target == 0:
            return True
        if idx == len(nums):
            return False
        if dp[target] != -1:
            return True if dp[target] else False
        
        if target < nums[idx]:
            dp[target] = self.dfs(idx+1, nums, target, dp)
            return True if dp[target] else False         
        #inclusion
        option1 = self.dfs(idx+1, nums, target - nums[idx], dp)
        #exclusion
        option2 = self.dfs(idx+1, nums, target, dp)
        dp[target] = option1 or option2
        return True if dp[target] else False

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total//2
        dp = [-1] * (target+1)
        return self.dfs(0, nums, target, dp)                 


