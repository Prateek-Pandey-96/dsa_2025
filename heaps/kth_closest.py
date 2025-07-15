from typing import List
from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heappush(heap, (-1 * ((point[0]*point[0])+(point[1]*point[1])), point))
            if len(heap) > k:
                heappop(heap)

        result = []

        while heap:
            _, point = heappop(heap)
            result.append(point)

        return result
