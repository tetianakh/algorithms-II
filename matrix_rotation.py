def rotate(matrix):
    """Rotates a matrix clockwise by 90 degrees."""
    rows = len(matrix)
    cols = len(matrix[0])
    # dimentions of the rotated matrix
    new_cols, new_rows = rows, cols

    # initialize the rotated matrix
    new_matrix = []
    for i in range(new_rows):
        new_matrix.append([None for _ in range(new_cols)])

    # copy values into the rotated matrix
    for i in range(rows):
        for j in range(cols):
            # 1st column becomes 1st row, last column becomes last row
            # 1st row becomes last column, last row becomes first column
            new_i = j
            new_j = new_cols - i - 1
            new_matrix[new_i][new_j] = matrix[i][j]

    return new_matrix


def test_rotate():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    result = rotate(matrix)
    expected = [
        [4, 1],
        [5, 2],
        [6, 3],
    ]
    assert result == expected
