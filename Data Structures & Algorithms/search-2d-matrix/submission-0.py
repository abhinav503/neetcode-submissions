class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rLen = len(matrix)
        cLen = len(matrix[0]) if rLen > 0 else 0
        l, r = 0, (rLen * cLen) - 1
        while l <= r:
            mid = l + (r-l) // 2
            row = mid // cLen
            col = mid % cLen

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
