from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        robbed = nums[0]
        unrobbed = 0

        for i in range(1, n):
            new_robbed = nums[i] + unrobbed
            new_unrobbed = max(robbed, unrobbed)
            robbed = new_robbed
            unrobbed = new_unrobbed

        return max(robbed, unrobbed)

