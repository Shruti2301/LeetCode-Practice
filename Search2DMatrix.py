class Solution(object):
    def searchMatrix(self, matrix, target):
       
        # Check if the matrix is empty
        if matrix == []:
            return False
        else:
            # Get the number of rows and columns in the matrix
            no_rows = len(matrix)
            no_cols = len(matrix[0])
            
            # Compare the target with the first and last elements of the matrix
            if target < matrix[0][0] or target > matrix[no_rows - 1][no_cols - 1]:
                return False
            
            # Start from the top-right corner of the matrix
            r = 0
            c = no_cols - 1
            
            # Iterate until we reach the bottom-left corner of the matrix
            while r < no_rows and c >= 0:
                # If the target is found, return True
                if target == matrix[r][c]:
                    return True
                # If the target is greater than the current element, move downwards
                elif target > matrix[r][c]:
                    r += 1
                # If the target is less than the current element, move leftwards
                elif target < matrix[r][c]:
                    c -= 1
            # If the target is not found after the iteration, return False
            return False
