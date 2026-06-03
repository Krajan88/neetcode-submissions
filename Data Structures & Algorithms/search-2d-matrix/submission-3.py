class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if matrix[mid][-1] < target:
                top = mid + 1
            else:
                bottom = mid - 1

        if top == len(matrix):
            return False

        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[top][mid] < target:
                l = mid + 1
            elif matrix[top][mid] > target:
                r = mid - 1
            else:
                return True

        return False