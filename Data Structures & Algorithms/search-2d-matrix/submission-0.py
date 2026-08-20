class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outerL, outerR = 0, len(matrix) - 1
        width = len(matrix[0])
        while outerL <= outerR:
            outerMid = (outerL + outerR) // 2
            if target >= matrix[outerMid][0] and target <= matrix[outerMid][width - 1]:
                # TODO: mini binary search
                l, r = 0, width - 1
                while l <= r:
                    m = (l + r) // 2
                    if target == matrix[outerMid][m]:
                        return True
                    elif target > matrix[outerMid][m]:
                        l = m + 1
                    else:
                        r = m - 1
                break
            elif target < matrix[outerMid][0]:
                outerR = outerMid - 1
            else:
                outerL = outerMid + 1
        return False
        