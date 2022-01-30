#!/bin/python3
# https://www.hackerrank.com/challenges/non-divisible-subset/problem

import math


def nonDivisibleSubset(k, s):
    # The function is expected to return an INTEGER.
    # The function accepts following parameters:
    #  1. INTEGER k
    #  2. INTEGER_ARRAY s
    if k == 1:
        return 1

    r = 0
    reduced_counts = dict()
    for i in s:
        if i % k in reduced_counts:
            reduced_counts[i % k] += 1
        else:
            reduced_counts[i % k] = 1
    if k % 2 == 0 and k // 2 in reduced_counts:
        reduced_counts[k // 2] = 0
        r += 1
    if 0 in reduced_counts:
        reduced_counts[0] = 0
        r += 1

    for i in range(math.ceil(k / 2)):
        r += max(reduced_counts.get(i, 0), reduced_counts.get(k - i, 0))
    return r


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))

    print(nonDivisibleSubset(k, s))
