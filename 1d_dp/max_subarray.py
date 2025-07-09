from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        curr_max = nums[0]
        global_max = curr_max

        for i in range(1, n):
            curr_max = max(curr_max + nums[i], nums[i])
            global_max = max(global_max, curr_max)

        return global_max 
