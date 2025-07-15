from typing import List
from heapq import heappush, heappop 

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            heappush(self.heap, num)
        

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        
        while len(self.heap) > self.k:
            heappop(self.heap)

        kth_largest = heappop(self.heap)
        heappush(self.heap, kth_largest)
        return kth_largest

