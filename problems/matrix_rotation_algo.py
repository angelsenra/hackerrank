#!/bin/python3
# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

def matrixRotation(matrix, number_of_rotations):
    # The function accepts following parameters:
    #  1. 2D_INTEGER_ARRAY matrix
    #  2. INTEGER number_of_rotations
    #
    height = len(matrix)
    width = len(matrix[0])
    final_matrix = [["." for _ in range(width)] for _ in range(height)]

    rotations = list()
    for level in range(min(width, height) // 2):
        rotation = list()
        x = y = level
        while y < (height - level) - 1:
            rotation.append([y, x])
            y += 1
        while x < (width - level) - 1:
            rotation.append([y, x])
            x += 1
        while y > level:
            rotation.append([y, x])
            y -= 1
        while x > level:
            rotation.append([y, x])
            x -= 1
        rotations.append(rotation)

    for rotation in rotations:
        for a, p in enumerate(rotation):
            q = rotation[(a + number_of_rotations) % len(rotation)]
            if rotation == rotations[0] and (q[0] > height or p[0] > height):
                return
            final_matrix[q[0]][q[1]] = matrix[p[0]][p[1]]

    return("\n".join(" ".join(row) for row in final_matrix))


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    number_of_rotations = int(first_multiple_input[2])

    matrix = []
    for _ in range(m):
        matrix.append(list(map(str, input().rstrip().split())))

    print(matrixRotation(matrix, number_of_rotations))
