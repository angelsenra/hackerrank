#!/bin/python3


def surfaceArea(A):
    # The function is expected to return an INTEGER.
    # The function accepts 2D_INTEGER_ARRAY A as parameter.
    area = 0
    height = len(A)
    width = len(A[0])

    # Step 1. Top and bottom
    area += sum(2 for row in A for n in row if n > 0)

    # Step 2. For each level, area of the figure
    for level in range(max(n for row in A for n in row)):
        for y in range(height):
            for x in range(width):
                if A[y][x] - 1 < level:
                    continue

                for (dy, dx) in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    is_out_of_map = not ((0 <= y + dy < height) and (0 <= x + dx < width))
                    is_shorter_than_level = not is_out_of_map and A[y + dy][x + dx] - 1 < level
                    if is_out_of_map or is_shorter_than_level:
                        area += 1

    return area


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    H = int(first_multiple_input[0])
    W = int(first_multiple_input[1])

    A = []
    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    print(surfaceArea(A))
