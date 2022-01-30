#!/bin/python3
# https://www.hackerrank.com/challenges/queens-attack-2/problem


def queensAttack(n, k, r_q, c_q, obstacles):
    # The function is expected to return an INTEGER.
    # The function accepts following parameters:
    #  1. INTEGER n
    #  2. INTEGER k
    #  3. INTEGER r_q
    #  4. INTEGER c_q
    #  5. 2D_INTEGER_ARRAY obstacles
    obstacles = set((i[0] - 1, i[1] - 1) for i in obstacles)
    result = 0
    for r_step in [-1, 0, 1]:
        for c_step in [-1, 0, 1]:
            if r_step == c_step == 0:
                continue
            r = r_q - 1 + r_step
            c = c_q - 1 + c_step
            while (0 <= r < n) and (0 <= c < n):
                if (r, c) in obstacles:
                    break
                result += 1
                r += r_step
                c += c_step
    return result

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])

    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    print(queensAttack(n, k, r_q, c_q, obstacles))
