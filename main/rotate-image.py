class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Traverse the matrix in layers
        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer

            for i in range(first, last):
                offset = i - first

                # Save top
                top = matrix[first][i]

                # Move left to top
                matrix[first][i] = matrix[last - offset][first]

                # Move bottom to left
                matrix[last - offset][first] = matrix[last][last - offset]

                # Move right to bottom
                matrix[last][last - offset] = matrix[i][last]

                # Move top to right
                matrix[i][last] = top