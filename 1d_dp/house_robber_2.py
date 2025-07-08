from typing import List

class Solution:
    def helper(self, nums: List[int]) -> int:
        n = len(nums)

        robbed = nums[0]
        unrobbed = 0

        for i in range(1, n):
            new_robbed = nums[i] + unrobbed
            new_unrobbed = max(robbed, unrobbed)
            robbed = new_robbed
            unrobbed = new_unrobbed

        return max(robbed, unrobbed)

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:n-1]))
