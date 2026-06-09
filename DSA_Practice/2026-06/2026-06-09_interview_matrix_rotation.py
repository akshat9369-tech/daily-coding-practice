"""Matrix Rotation: Rotate Image 90 Degrees In-Place."""

def rotate_matrix(matrix: list[list[int]]) -> None:
    n = len(matrix)

    # Step 1: Transpose matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_matrix(mat)
    print("Rotated 90 degrees clockwise:")
    for row in mat:
        print(" ", row)
