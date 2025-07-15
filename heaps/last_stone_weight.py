from typing import List
from heapq import heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heappush(heap, -stone)

        while len(heap) > 1:
            top = heappop(heap)
            second_top = heappop(heap)

            if top == second_top:
                continue
            else:
                heappush(heap, -abs(top-second_top))

        result = 0
        if len(heap) == 1:
            result = heappop(heap)
        return -result
