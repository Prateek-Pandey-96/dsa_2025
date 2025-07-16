from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        low, high = 0, m-1
        row = - 1
        while low <= high:
            mid = low + (high-low)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                high = mid-1
            else:
                row = mid
                low = mid + 1
        
        if row == -1:
            return False
        
        low, high = 0, n-1
        while low <= high:
            mid = low + (high-low)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                high = mid-1
            else:
                low = mid+1

        return False
