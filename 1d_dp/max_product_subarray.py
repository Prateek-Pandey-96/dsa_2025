from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        
        pref, suff = 1, 1
        result = float("-inf")
        
        for i in range(n):
            pref = pref * nums[i]
            suff = suff * nums[n-1-i]

            result = max(result, pref, suff)
            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1

        return int(result)
