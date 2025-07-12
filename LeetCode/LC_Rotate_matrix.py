def rotate_image(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

    return matrix






image = [
    [1, 2, 3],        
    [4, 5, 6],
    [7, 8, 9]
]

        # [7, 4, 1]
        # [8, 5, 2]
        # [9, 6, 3]   this is output rotated 90 degree

rotated = rotate_image(image)

for i in rotated:
    print(i)