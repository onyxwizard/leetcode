class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Step 1: Use the first row and first column as markers
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        # Step 2: Mark rows and columns that need to be zeroed
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the row
                    matrix[0][j] = 0  # Mark the column

        # Step 3: Zero out cells based on markers in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 4: Zero out the first row if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Step 5: Zero out the first column if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
        return matrix
if __name__ == "__main__":
    zero = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print(zero.setZeroes(matrix))